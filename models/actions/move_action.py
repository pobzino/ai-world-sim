from dataclasses import dataclass
from models.actions.action import Action

@dataclass
class MoveAction(Action):
    range: float


    
