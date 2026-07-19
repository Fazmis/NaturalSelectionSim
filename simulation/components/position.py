from .base_component import BaseComponent
from dataclasses import dataclass

@dataclass(slots=True)
class Position(BaseComponent):
    x: int = 0
    y: int = 0
