from dataclasses import dataclass
from models.actions.action import Action


@ dataclass
class ActionInstance:
    action: Action
    status: str
    target: str
    result : str
