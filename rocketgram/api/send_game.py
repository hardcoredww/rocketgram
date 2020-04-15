# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .request import Request
from .utils import INLINE_KEYBOARDS


@dataclass(frozen=True)
class SendGame(Request):
    """\
    Represents SendGame request object:
    https://core.telegram.org/bots/api#sendgame
    """

    method = "sendGame"

    chat_id: int
    game_short_name: str
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[INLINE_KEYBOARDS] = None