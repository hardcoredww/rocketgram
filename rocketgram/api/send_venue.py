# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import ALL_KEYBOARDS


@dataclass(frozen=True)
class SendVenue(Request):
    """\
    Represents SendVenue request object:
    https://core.telegram.org/bots/api#sendvenue
    """

    method = "sendVenue"

    chat_id: Union[int, str]
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[ALL_KEYBOARDS] = None