# custom filter
- Define function with decorator like below
```
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')
```
- Now you can use it in template like below.
```
{{variable|cut}}
```

# formset
We can handle multiple object of same model class using formset. ie. we can take multiple article from user simulteneously
```
from django.forms import formset_factory

# creating a formset and 5 instances of GeeksForm
GeeksFormSet = formset_factory(GeeksForm, extra = 5) # GeekForm is normal form whose 5 instance will be created
formset = GeeksFormSet()
```

