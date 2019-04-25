# Copyright (C) 2015-2019 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


import asyncio
import logging
import signal
from typing import TYPE_CHECKING, Union, Dict, List, Set

try:
    import ujson as json
except ModuleNotFoundError:
    import json

from aiohttp import web

from ..types import InputFile
from .executor import Executor
from ..requests import Request, GetMe, GetUpdates, SetWebhook, DeleteWebhook
from ..update import Update
from ..errors import RocketgramRequestError

if TYPE_CHECKING:
    from ..bot import Bot

logger = logging.getLogger('rocketgram.executors.webhook')


class WebHooksExecutor(Executor):
    def __init__(self, base_url: str, base_path: str, *, host: str = 'localhost',
                 port: int = 8080):
        """

        :param base_url:
        :param base_path:
        :param host:
        :param port:
        """

        self.__base_url = base_url
        self.__base_path = base_path
        self.__host = host
        self.__port = port

        self.__bots = dict()
        self.__srv = None
        self.__started = False

        self.__tasks: Dict[Bot, Set[asyncio.Task]] = dict()

    @property
    def bots(self):
        """

        :return:
        """
        return self.__bots.values()

    @property
    def running(self):
        """

        :rtype: object
        """
        return self.__started

    def can_process_webhook_request(self, request: Request) -> bool:
        for k, v in request.render().items():
            if isinstance(v, InputFile):
                return False

        return True

    async def add_bot(self, bot: 'Bot', *, suffix=None, webhook=True, drop_updates=False,
                      max_connections=None):
        """

        :param bot:
        :param suffix:
        :param webhook:
        :param drop_updates:
        :param max_connections:
        """
        if bot in self.__bots.values():
            raise ValueError('Bot already added.')

        if not suffix:
            suffix = bot.token

        full_path = self.__base_path + suffix
        full_url = self.__base_url + suffix

        if bot.name is None:
            response = await bot.send(GetMe())
            bot.name = response.result.username
            logger.info('Bot authorized as @%s', response.result.username)

        await bot.init()

        if drop_updates:
            await bot.send(DeleteWebhook())
            offset = 0
            while True:
                resp = await bot.send(GetUpdates(offset + 1))
                if not len(resp.result):
                    break
                for update in resp.result:
                    if offset < update.update_id:
                        offset = update.update_id
            logger.debug('Updates dropped for @%s', bot.name)

        self.__bots[full_path] = bot
        logger.info('Added bot @%s', bot.name)

        if webhook or drop_updates:
            await bot.send(SetWebhook(full_url, max_connections=max_connections))
            logger.debug('Webhook setup done for bot @%s', bot.name)

    async def remove_bot(self, bot: 'Bot', webhook=True):
        """

        :param bot:
        :param webhook:
        """
        if bot not in self.__bots.values():
            raise ValueError('Bot was not found.')

        self.__bots = {k: v for k, v in self.__bots.items() if v != bot}

        if bot in self.__tasks:
            tasks = self.__tasks[bot]
            self.__tasks[bot] = set()
            await self.__wait_tasks(tasks)

        if webhook:
            try:
                await bot.send(DeleteWebhook())
            except RocketgramRequestError:
                logger.error('Error while removing webhook for %s.' % bot.name)

        await bot.shutdown()

        logger.info('Removed bot @%s', bot.name)

    async def start(self):
        """

        :return:
        """

        async def __handler(request: web.BaseRequest):
            if request.method != 'POST':
                return web.Response(status=400, text="Bad request.")

            bot: 'Bot' = self.__bots.get(request.path)

            if not bot:
                logger.warning("Bot not found for request '%s %s'.", request.method, request.path)
                return web.Response(status=404, text="Not found.")

            if not bot in self.__tasks:
                self.__tasks[bot] = set()

            parsed = Update.parse(json.loads(await request.read()))

            task = asyncio.create_task(
                bot.process(self, parsed))
            self.__tasks[bot].add(task)

            response: Request = await task
            if response:
                data = json.dumps(response.render(with_method=True))
                return web.Response(body=data, headers={'Content-Type': 'application/json'})

            self.__tasks[bot] = {t for t in self.__tasks[bot] if not t.done()}

            return web.Response(status=200)

        if self.__started:
            return

        self.__started = True

        logger.info("Starting with webhooks...")

        loop = asyncio.get_event_loop()

        logger.info("Listening on http://%s:%s%s", self.__host, self.__port, self.__base_path)
        self.__srv = await loop.create_server(web.Server(__handler), self.__host, self.__port, backlog=128)

        logger.info("Running!")

    async def __wait_tasks(self, tasks: Set[asyncio.Task]):
        while len(tasks):
            logger.info("Waiting %s tasks...", len(tasks))
            _, tasks = await asyncio.wait(tasks, timeout=1, return_when=asyncio.FIRST_COMPLETED)

    async def stop(self):
        """

        :return:
        """
        logger.info("Stopping server...")

        if not self.__started:
            return

        self.__started = False

        if self.__srv:
            self.__srv.close()
            await self.__srv.wait_closed()
            self.__srv = None

        tasks = set()
        for b, t in self.__tasks.items():
            tasks.update(t)
            t.clear()

        await self.__wait_tasks(tasks)

        logger.info("Stopped.")

    @classmethod
    def run(cls, bots: Union['Bot', List['Bot']], base_url: str, base_path: str, *, host='0.0.0.0', port=8080,
            webhook_setup=True, webhook_remove=True, drop_updates=False,
            signals: tuple = (signal.SIGINT, signal.SIGTERM), request_timeout=30, shutdown_wait=10):

        """

        :param bots:
        :param drop_updates:
        :param signals:
        :param request_timeout:
        :param shutdown_wait:
        """

        executor = cls(base_url, base_path, host=host, port=port)

        def add(bot: 'Bot'):
            return executor.add_bot(bot, webhook=webhook_setup, drop_updates=drop_updates)

        def remove(bot: 'Bot'):
            return executor.remove_bot(bot, webhook=webhook_remove)

        logger.info('Starting webhook executor...')
        logger.debug('Using base url: %s', base_url)
        logger.debug('Using base path: %s', base_path)

        cls._run(executor, add, remove, bots, signals, )
