from .base_component import BaseComponent
from dataclasses import dataclass

@dataclass(slots=True)
class Health(BaseComponent):
    hp: int = 1
