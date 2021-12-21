Python module search path
- built in modules
- sys.path
 The search is in this order.

The current directory.
PYTHONPATH (an environment variable with a list of directories).
The installation-dependent default directory

To reload the module
>>> import my_module
>>> imp.reload(my_module)

We can use the dir() function to find out names that are defined inside a module

- multiple and multilevel inheritance
In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching the same class twice.

example
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object]. This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).

MRO of a class can be viewed as the __mro__ attribute or the mro() method. The former returns a tuple while the latter returns a list.

>>> MultiDerived.__mro__
(<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>)

>>> MultiDerived.mro()
[<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>]


 - Operator Overloading
 the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings

- Overloading the + Operator
To overload the + operator, we will need to implement __add__() function in the class. With great power comes great responsibility. We can do whatever we like, inside this function. But it is more sensible to return a Point object of the coordinate sum.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)
# output: (3,5) 

What actually happens is that, when you use p1 + p2, Python calls p1.__add__(p2) which in turn is Point.__add__(p1,p2). After this, the addition operation is carried out the way we specified.

Similarly, we can overload other operators as well. The special function that we need to implement is tabulated below

Operator	                Expression	    Internally
Addition	                p1 + p2	        p1.__add__(p2)
Subtraction	                p1 - p2	        p1.__sub__(p2)
Multiplication	            p1 * p2	        p1.__mul__(p2)
Power	                    p1 ** p2	    p1.__pow__(p2)
Division	                p1 / p2	        p1.__truediv__(p2)
Floor Division	            p1 // p2	    p1.__floordiv__(p2)
Remainder (modulo)	        p1 % p2	        p1.__mod__(p2)
Bitwise Left Shift	        p1 << p2	    p1.__lshift__(p2)
Bitwise Right Shift	        p1 >> p2	    p1.__rshift__(p2)
Bitwise AND	                p1 & p2	        p1.__and__(p2)
Bitwise OR	                p1 | p2	        p1.__or__(p2)
Bitwise XOR	                p1 ^ p2	        p1.__xor__(p2)
Bitwise NOT	                ~p1	            p1.__invert__()



- Overloading the + Operator
# overloading the less than operator
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(1,-1)

# use less than
print(p1<p2)
print(p2<p3)
print(p1<p3)

# Output

True
False
False


Operator	                Expression	        Internally
Less than	                p1 < p2	            p1.__lt__(p2)
Less than or equal to	    p1 <= p2	        p1.__le__(p2)
Equal to	                p1 == p2	        p1.__eq__(p2)
Not equal to	            p1 != p2	        p1.__ne__(p2)
Greater than	            p1 > p2	            p1.__gt__(p2)
Greater than or equal to	p1 >= p2	        p1.__ge__(p2)

# Generator
Both yield and return will return some value from a function.

The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.

example
# A simple generator function
```
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
```
- generator to reverse the string
```
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)
```    

- creating generator using generator expression
```
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)
```

- use case
```
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result
```

can be done easily using below
```
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
```


- list vs tuple
The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified. Tuples are more memory efficient than the lists


- shallow copy vs deepcopy
A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original. A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

= is shallow copy for list but deep copy for int

import copy
copy.copy(x)
copy.deepcopy(x)
Here, the copy() return a shallow copy of x. Similarly, deepcopy() return a deep copy of x.


# gone through this
deep and shallow copy in python
https://www.programiz.com/python-programming/shallow-deep-copy

# collection
https://realpython.com/python-collections-module/

# oop
you can access class attribute using 
obj.__class__.attr_name also directly accisible obj.attr_name
https://www.programiz.com/python-programming/object-oriented-programming

```
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3) # or you can use super().__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

```

class Shape():
    pass

class Polygon(Shape):
    pass

class Triangle(Polygon):
    pass

t = Triangle()
isinstance(t, Shape) # True

isinstance relationship is recursive till object. as every thing in python is inherited from "object" class
so we can use isinstance, and issubclass method to know parent class of object or class.

# operator overloading
https://www.programiz.com/python-programming/operator-overloading

# property
Whenever we assign or retrieve any object attribute like temperature as shown above, Python searches it in the object's built-in __dict__ dictionary attribute.

>>> human.__dict__
{'temperature': 37}
Therefore, man.temperature internally becomes man.__dict__['temperature']

