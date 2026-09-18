from dataclasses import dataclass

#Define data class - ideal model of what agent contains

@dataclass
class Agent:
    name: str
    id: str
    position: tuple[float, float]
    faction_id: str
    health: int = 100 #Python dataclasses don’t allow a required field after defaulted fields. Put the required fields first conceptually:
    strength: int = 10
    max_stamina: int = 100
    stamina: int = 100
    incapacitated: bool = False
    status: list[str]