from dataclasses import dataclass
from pympler import asizeof
from timeit import timeit

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ["name", "lon","lat"]
    name: str
    lon: float
    lat: float

# checking memory usage
simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('London', -0.1, 51.5)

print(asizeof.asizeof(simple))
print(asizeof.asizeof(slot))

# checking accessing speed
print(timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 10.8)", globals=globals()))
print(timeit("slot.name", setup="slot=SlotPosition('Oslo', 10.8, 10.8)", globals=globals()))

