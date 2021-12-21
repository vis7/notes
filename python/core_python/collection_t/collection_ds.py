# https://realpython.com/python-collections-module/ # see just the code read explaination if needed

# Named tuple
from collections import namedtuple

Point = namedtuple("point", ["x", "y"])
p = Point(10,20)

# print(p)
# print(p.x)
# print(p.y)

# print(p[0])
# print(p[1])

# default value
Point = namedtuple("point", ["x", "y"], defaults=[10,20])
p = Point(30,40)

print(p)

