# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional, List

from .input_file import InputFile
from .mask_position import MaskPosition
from .request import Request


@dataclass(frozen=True)
class AddStickerToSet(Request):
    """\
    Represents AddStickerToSet request object:
    https://core.telegram.org/bots/api#addstickertoset
    """

    method = "addStickerToSet"

    user_id: int
    name: str
    png_sticker: Optional[Union[InputFile, str]]
    tgs_sticker: Optional[InputFile]
    emojis: str
    mask_position: Optional[MaskPosition] = None

    def files(self) -> List[InputFile]:
        files = list()
        if isinstance(self.png_sticker, InputFile):
            files.append(self.png_sticker)
        if self.tgs_sticker is not None:
            files.append(self.tgs_sticker)
        return files
