# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .input_message_content import InputMessageContent
from .parse_mode_type import ParseModeType


@dataclass(frozen=True)
class InputTextMessageContent(InputMessageContent):
    """\
    Represents InputTextMessageContent object:
    https://core.telegram.org/bots/api#inputtextmessagecontent
    """

    message_text: str
    parse_mode: Optional[ParseModeType] = None
    disable_web_page_preview: Optional[bool] = None
