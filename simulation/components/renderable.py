from .base_component import BaseComponent
from dataclasses import dataclass

@dataclass(slots=True)
class RenderAble(BaseComponent):
    shape: str = "circle"
    size: int = 10
    color: tuple[int, int, int] = (0, 255, 0)
