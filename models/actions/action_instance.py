from dataclasses import dataclass
from models.actions.action import Action


@ dataclass
class ActionInstance:
    action: Action
    target: tuple[float, float]
    result : str

