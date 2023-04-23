
from typing import Final
from enum import IntEnum, EnumMeta

__all__ = [
    'Materials'
]

class Materials(IntEnum, metaclass=EnumMeta):
    Default = 0
    Tarmac = 1
    TarmacDamaged = 2
    TarmacReallyDamaged = 3
