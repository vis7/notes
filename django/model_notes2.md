 # django field options (atrtributes)
null
blank
choices
default
help_text
primary_key
unique
verbose_name - it is also fist positional argument

# relationship - 
a recursive relationship can be defined and references to as-yet undefined models can be made. on ManyToMany, Foreignkey and OneToOneField.


- many-to-one- ForeignKey() is used  - modelname (postional arguemnt) and on_delete

For example, if a Car model has a Manufacturer – that is, a Manufacturer makes multiple cars but each Car only has one Manufacturer – use the following definitions:
```
from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
```

many-to-many - ManyToManyField() is used - modelname (postional arguemnt)
- For example, if a Pizza has multiple Topping objects – that is, a Topping can be on multiple pizzas and each Pizza has multiple toppings – here’s how you’d represent that:
- It doesn’t matter which model has the ManyToManyField, but you should only put it in one of the models – not both.
- It’s suggested, but not required, that the name of a ManyToManyField (toppings in the example above) be a plural describing the set of related model objects.



one-to-one - OneToOneField requires a positional argument: the class to which the model is related.


- It’s perfectly OK to relate a model to one from another app. To do this, import the related model at the top of the file where your model is defined. Then, refer to the other model class wherever needed.

Field name restrictions
- A field name cannot be a Python reserved word
- A field name cannot contain more than one underscore in a row, due to the way Django’s query lookup syntax works.
- A field name cannot end with an underscore, for similar reasons.

# Meta options
- Attributes
    - ordering
    - verbose_name_plural

# Model Inheritance
There are three styles of inheritance that are possible in Django.
## Abstract Base Class
You write your base class and put abstract=True in the Meta class. This model will then not be used to create any database table. Instead, when it is used as a base class for other models, its fields will be added to those of the child class.


## Multi-table inheritance 
It inherit table without declaring base class as abstract. so data of base class will be saved inside the table of base class

## Proxy models
It is like view on sql. It has all attribute as main table but you can have diffrent ordering and maybe some other features like that

In Django, a proxy model is a special type of model that doesn't have its own database table, but rather "proxies" or "forwards" all operations to a parent model. This allows you to create a model that behaves the same as an existing model, but with additional or modified behavior.

Proxy models can be useful in a variety of situations. For example, you might use a proxy model to add custom methods to an existing model, or to override the default behavior of an existing model in a specific context.

usage
- To add custom managers to an existing model
- To override the default __str__ method of an existing model:
- To modify the default ordering of an existing model
- To add a custom field to an existing model



