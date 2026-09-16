from dataclasses import dataclass
from models.agent import Agent #importing the dataclasses from their respective files
from models.faction import Faction
from models.location import Location
from models.zone import Zone


@dataclass
class World:
    agents: list[Agent]
    locations: list[Location]
    factions: list[Faction]    
    zones: list[Zone]
    current_turn: int
    event_history: list[str]
