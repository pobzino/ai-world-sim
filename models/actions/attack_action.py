from dataclasses import dataclass
from models.actions.action import Action

@dataclass
class AttackAction(Action):
    range: float
    base_damage: int
    damage_type: str



