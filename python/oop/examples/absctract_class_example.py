from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(Polygon):
    def no_of_sides(self):
        print("I have three sides")

class Pentagon(Polygon):
    def no_of_sides(self):
        print("I have five sides")

class Hectagon(Polygon):
    def no_of_sides(self):
        print("I have six sides")

class Quadrilateral(Polygon):
    def no_of_sides(self):
        print("I have four sides")


# Can't create object of Abstract class
# p = Polygon()
# print(p.no_of_sides())

t = Triangle()
t.no_of_sides()

p = Pentagon()
p.no_of_sides()

h = Hectagon()
h.no_of_sides()

q = Quadrilateral()
q.no_of_sides()



