
from typing import Any, Sequence

from .set import XML
from .color import ColorRGBA
from .materials import Materials

__all__ = [
    'Layer',
    'ColorRGBA',
    'Materials',
    'XML'
]

class Layer:
    def __init__(self, id: int) -> None:
        self.content: Sequence[str] = []
        self.content.append('        <layer>')
        self.addSomething('id', id)
        self.addSomething('cameraInputTarget', 1)
    
    def addSomething(self, name: str, value: Any) -> None:
        self.content.append(f'            <{name}>{value}</{name}>')
    
    def addColor(self, color: ColorRGBA) -> None:
        self.addSomething('colorR', color.red)
        self.addSomething('colorG', color.green)
        self.addSomething('colorB', color.blue)
        self.addSomething('colorA', color.alpha)
    
    def addMaterial(self, material: Materials) -> None:
        self.addSomething('category', material.value)
    
    def addRotation(self, rotation: float) -> None:
        self.addSomething('rotation', rotation)

    def addSize(self, x: float, y: float) -> None:
        self.addSomething('sizeX', x)
        self.addSomething('sizeY', y)
    
    def addPosition(self, x: float, y: float) -> None:
        self.addSomething('posX', x)
        self.addSomething('posY', y)
    
    def addIsErase(self, value: bool) -> None:
        self.addSomething('erase', int(value))

    def addIsMirrored(self, value: bool) -> None:
        self.addSomething('mirrored', int(value))
    
    def compile(self) -> Sequence[str]:
        self.content.append('        </layer>')
        return self.content

