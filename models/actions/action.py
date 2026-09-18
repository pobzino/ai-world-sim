from dataclasses import dataclass

@dataclass
class Action():
    name: str
    effect: str
    id: str
    type: str
    stamina_use: int

