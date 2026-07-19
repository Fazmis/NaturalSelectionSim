from .base_component import BaseComponent
from dataclasses import dataclass

@dataclass(slots=True)
class Velocity(BaseComponent):
    speed_x: int = 0
    speed_y: int = 0