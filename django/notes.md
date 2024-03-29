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


# Permission
Token Authentication
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]

f successfully authenticated, TokenAuthentication provides the following credentials.

request.user will be a Django User instance.
request.auth will be a rest_framework.authtoken.models.Token instance.

Unauthenticated responses that are denied permission will result in an HTTP 401 Unauthorized response with an appropriate WWW-Authenticate header.

login - authentication
roles - authorization


from rest_framework import permissions

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
        return not blocked

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user



# to start ngrok
ngrok http 8000

# General
+ https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
+ first validate_field run then validate method run

token = Token.objects.get_or_create(user=request.user)[0].key




- first values will be store in db, second will be shown to users
MANIFEST_TYPES = (
    (LOCAL, 'Local'),
    (INTER_BRANCH, 'Inter Branch')
)
