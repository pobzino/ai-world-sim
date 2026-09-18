from dataclasses import dataclass
from models.actions.action import Action

@dataclass
class WaitAction(Action):
    stamina_recovery: int = 10



    
