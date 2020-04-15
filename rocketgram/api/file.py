# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class File:
    """\
    Represents File object:
    https://core.telegram.org/bots/api#file
    """

    file_id: str
    file_unique_id: str
    file_size: Optional[int]
    file_path: Optional[str]

    @classmethod
    def parse(cls, data: dict) -> Optional['File']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_unique_id'], data.get('file_size'), data.get('file_path'))
