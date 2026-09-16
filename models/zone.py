from dataclasses import dataclass

@dataclass
class Zones:
    id: str
    name: str
    location_name: str
    faction_id: str
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    zone_type: str
    description: str