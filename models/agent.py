from dataclasses import dataclass

#Define data class - ideal model of what agent contains

@dataclass
class Agent:
    name: str
    id: str
    location: str
    position: tuple[float, float]
    faction_id: str
    health: int = 100 #Python dataclasses don’t allow a required field after defaulted fields. Put the required fields first conceptually:
    strength: int = 10