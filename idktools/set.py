
from typing import Sequence

__all__ = [
    'XML'
]

class XML:
    def __init__(self, name: str) -> None:
        global NowXML
        self.content: Sequence[str] = []
        self.content.append("<xml>")
        self.content.append(f"    <set name=\"{name}\">")
        NowXML = self
    
    def add(self, data: Sequence[str]) -> None:
        self.content += data

    def create(self) -> None:
        self.content.append(f"    </set>")
        self.content.append("</xml>")
        with open('mod.xml', 'w') as f:
            f.write('\n'.join(self.content))

