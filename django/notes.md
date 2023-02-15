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
formset = GeeksFormSet() # we can now use it as normal form
```

# authentication
https://studygyaan.com/django/how-to-extend-django-user-model


#
- To dump data:
```
python manage.py dumpdata app.model_name --indent 4 > fixtures/model_name.json
```
- To load data:
```
python manage.py loaddata fixtures/model_name.json --app app.model_name
```

- force login user
self.client.force_login(user1)
self.client.login(username='user1', password='Use@1234')

- In django test objects created are stay only in that function (test case). In other function that are not available.

