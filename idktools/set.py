
from typing import Sequence

__all__ = [
    'XML'
]

class XML:
    def __init__(self, name: str) -> None:
        self.content: Sequence[str] = []
        self.content.append("<xml>")
        self.content.append(f"    <set name=\"{name}\">")
    
    def add(self, data: Sequence[str]) -> None:
        self.content += data

    def create(self) -> None:
        self.content.append(f"    </set>")
        self.content.append("</xml>")
        with open('generated.xml', 'w') as f:
            f.write('\n'.join(self.content))

