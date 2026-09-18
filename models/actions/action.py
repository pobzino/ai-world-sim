from dataclasses import dataclass

@dataclass
class Action():
    name: str
    effect: str
    id: str
    stamina_use: int

