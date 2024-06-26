Python module search path
- built in modules
- sys.path
- serach in current file position

The current directory.
PYTHONPATH (an environment variable with a list of directories).
The installation-dependent default directory

To reload the module
>>> import imp
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



- Overloading the Comparision Operator
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


# notes
The discard() method removes the specified item from the set.

This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.


https://www.geeksforgeeks.org/class-method-vs-static-method-python/

# python
txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)

=> banana

# walrus operator
Introduced in python 3.8, the walrus operator, (:=), formally known as the assignment expression operator, offers a way to assign to variables within an expression, including variables that do not exist yet. As seen above, with the simple assignment operator (=), we assigned num = 15 in the context of a stand-alone statement.

An expression evaluates to a value. A statement does something.

In other words, the walrus operator allows us to both assign a value to a variable, and to return that value, all in the same expression. The name is due to its similarity to the eyes and tusks of a Walrus on its side.

name := expr

assigne value if not exist, compare if exist 


>>> num1 = 15 
>>> if num2:= num1:
...     print('yes')
... 
yes
>>> num2
15


expr is evaluated and then assigned to the variable name. That value will also be returned.



>>> print(num:=15)
15


#########################
for else - else will excecute only if whole for loop completed
exception else - else will executed only if exception not occured

#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
  raise Exception("something went wrong exception raised")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("print from finally block")
 
print("program completed execution")

###############

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("from else of for")

#If the loop breaks, the else block is not executed.
print("Finally finished!")

#################

JIT Compliler
The JIT compiler helps improve the performance of Java programs by compiling bytecodes into native machine code at run time

Cpython does not have JIT, Pypi, Jython, IornPython have, but they don't impliemnt all python subversions


# need to do practice
closure
    - create multiple of 3, 5 closure
    - Print Odd Numbers using Python Closure

decorators
lambda functions
complex list comprehention


# ?
? nonlocal vs gloabal
-> "nonlocal" means that a variable is "neither local or global", i.e, the variable is from an enclosing namespace (typically from an outer function of a nested function).

An important difference between nonlocal and global is that a nonlocal variable must have been already bound in the enclosing namespace (otherwise an syntaxError will be raised) while a global declaration in a local scope does not require the variable is pre-bound (it will create a new binding in the global namespace if the variable is not pre-bound).


We can override below built in methods in class defined by us in python, we overrided len() but also listed remaining methods

class Order:
    def __init__(self, cart, name):
        self.cart = list(cart)
        self.name = name

    def __len__(self):
        return len(self.cart)

o = Order(['apple', 'banana', 'chery'], 'vishvajeet')
print(o)
print(len(o))


To Overloading operator there are built in methods
Airthmetic Operator
__add__()
__sub__()
__mul__()
__div__()
__divmod__()
__mod__() - Modulus of two number, remainder after devision. it. 10%3 = 1
__pow__

# methematical methods (built in)
__abs__
__len__()
__str__()
__repr__()
__bool__()
__abs__()
__ceil__
__floor__
__floordiv__
__sizeof__


# bitwise operators
__and__
__eq__
__ge__
__gt__
__le__
__lshift__
__lt__
__ne__
__or__
__xor__

above all methods have r methods ie. rand, rshift, rxor


Example of overriding rmethod


# decorator
=> pre requisite for decorators
we can define function inside function and call it
we can pass function as argument in function
function can return another function as return value

 A Python decorator is a function that takes in a function and returns it by adding some functionality.

 Basically, a decorator takes in a function, adds some functionality and returns it.

