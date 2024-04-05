# Inheritance
# if a field in a base class has a default value, then all new fields added in a subclass must have default values as well.

from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon : float = 0.0
    lat: float = 0.0

@dataclass
class Country(Position):
    country: str = "Unknown"
    lat: float = 40.0

spain = Country("Madrid", country="Spain")
print(spain)
# Then the order of the fields in Capital will still be name, lon, lat, country. However, the default value of lat will be 40.0.
