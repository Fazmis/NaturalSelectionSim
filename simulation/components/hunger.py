from dataclasses import dataclass
from .base_component import BaseComponent


@dataclass(slots=True)
class Hunger(BaseComponent):
    max_level: int = 100
    level: int = 100
