brief introduction about yourself and the projects you have worked on

# django
diffrence between flask, drf and fast api
limit number of request our api can return
how can we impliment middleware
restricting all api with some security constraint
pagination how to implement (django and drf)
improving performance of single api from 700 ms to 100 ms
nested serializer

# python
generator and iterater what they are how to use them 
decorators - also examples
property in python
Database insertion api efficiency


honesty(It's okay to not know everything. if you don't know then tell I don't know), calm, confidence. tell on things what you know. ask if you don't understand things clearly, ask about what work you will do if got selected, basic working of company, product based or service based.


inferenz 
opencv basic operations and django -drf, serializer various methods and attribute, raw sql query to do things fast.

# questions
- static method vs class method python

f,q and orm practicals
annotations and aggregations 
what is middleware ? how to write your own ?
django MVT architecture explain, viewset and routher
classbased views vs functionbased view and when to use which
inheritance in djanog (model inheritance, proxy inheritance) (https://buildatscale.tech/model-inheritance-in-django/)
authentication vs authorization 
serializers type in drf
apiview vs viewset diffrence
how to use sql queries in django
how can I use authentication in such a way that user can login from one device only
types of authentication

list vs tupple


*) what is mixin ? when to use ? how it is diffrent from class ? (https://stackoverflow.com/questions/860245/mixin-vs-inheritance)
-> Mixins are sometimes described as being "included" rather than "inherited". In short, the key difference from an inheritance is that mix-ins does NOT need to have a "is-a" relationship like in inheritance. From the implementation point of view, you can think it as an interface with implementations.

# git (go in depth)
cherrypick
rebase
how to convert 3 commit in to 1 commit

# database 
what is database indexing
what is diffrence if i do indexing or not do on performance

# practical task
```
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    salary = models.DecimalField()

    def __str__(self):
        return self.name

# queryset
from django.db.modesl import Q, F

q = Employee.objects.exclude(manager__isnull=True).filter(salary__gt=F(manager__salary))

# Share this in email

```

django 4.1 updates

# suggetions
- go in depth of things you knew, do practicals (annotations, orm, serializer)

# suggetions (Non Technical aspects)
- calm, confidence, decipline, honest, positive attitude



