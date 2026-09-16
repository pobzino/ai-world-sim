from dataclasses import dataclass

@dataclass
class Location:
    name: str
    width: float
    height: float
    land_description: str
    population: int
    control: dict[str,float] ##this defines the types inside the control dictionary, typically dictionaries us {"name": value}
