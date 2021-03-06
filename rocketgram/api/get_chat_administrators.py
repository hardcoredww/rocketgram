# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, List

from .request import Request
from .. import api


@dataclass(frozen=True)
class GetChatAdministrators(Request):
    """\
    Represents GetChatAdministrators request object:
    https://core.telegram.org/bots/api#getchatadministrators
    """

    chat_id: Union[int, str]

    def parse_result(self, data) -> List['api.ChatMember']:
        assert isinstance(data, list), "Should be list."
        return [api.ChatMember.parse(r) for r in data]

    async def send2(self) -> List['api.ChatMember']:
        res = await self._send()
        return res.result
