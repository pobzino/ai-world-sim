from dataclasses import dataclass

@dataclass
class Location:
    name: str
    land_description: str
    population: int
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    control: dict[str,float] ##this defines the types inside the control dictionary, typically dictionaries us {"name": value}
