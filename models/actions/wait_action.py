from dataclasses import dataclass
from models.actions.action import Action

@dataclass
class WaitAction(Action):
    range: float
    turns: int = 1
    recovery_per_turn: int = 10
    total_recovery = turns * recovery_per_turn



    
