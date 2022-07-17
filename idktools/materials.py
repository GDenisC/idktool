
from typing import Final
from enum import IntEnum, EnumMeta

__all__ = [
    'Materials'
]

class Materials(IntEnum, metaclass=EnumMeta):
    Default: Final[int] = 0
    Tarmac: Final[int] = 1
    Tarmac_damaged: Final[int] = 2
    Tarmac_really_damaged: Final[int] = 3
