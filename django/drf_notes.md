1. Serializer

from rest_framework import serializers
- other important serializer class
HyperlinkedModelSerializer

serializers.Serializer() # normal serializer
It impliment create(), update() internally

serializers.ModelSerializer

serializers.<Model>Field() # same fields as with django.models eg. CharField, IntegerField etc.
- other important fileds
PrimaryKeyRelatedField, HyperlinkedRelatedField



from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

- print representation of model
serializer = SnippetSerializer()
print(repr(serializer))



2. 

request.data | request.POST
def snippet_list(request, format=None): # at the end .json, .api or Accept:application/json, Accept:text/html in request header

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)

from rest_framework import status

- Wrapping API views
REST framework provides two wrappers you can use to write API views.

The @api_view decorator for working with function based views.
The APIView class for working with class-based views.

- These wrappers provide a few bits of functionality such as making sure you receive Request instances in your view, and adding context to Response objects so that content negotiation can be performed.

The wrappers also provide behaviour such as returning 405 Method Not Allowed responses when appropriate, and handling any ParseError exceptions that occur when accessing request.data with malformed input.

from rest_framework.decorators import api_view
from rest_framework.response import Response



3. class based view

from rest_framework.views import APIView

you can impliment get, post, patch, delete method in APIView class

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetriveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

4. Authentication and Permissions

to overriding existing save()
def save(self, *args, **kwargs):
    """
    Use the 'pygments' library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Snippet, self).save(*args, **kwargs)

The way we deal with that is by overriding a .perform_create() method on our snippet views, that allows us to modify how the instance save is managed, and handle any information that is implicit in the incoming request or requested URL.

On the SnippetList view class, add the following method:

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.


IsAuthenticatedOrReadOnly, which will ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access.

First add the following import in the views module

from rest_framework import permissions
Then, add the following property to both the SnippetList and SnippetDetail view classes.

permission_classes = [permissions.IsAuthenticatedOrReadOnly]

below will provide login/logout url
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

5. Relationships & HyperlinkedAPIs

from rest_framework.reverse import reverse

6. Viewsets and routers

from rest_framework import viewsets
- important viewsets
ReadOnlyModelViewSet

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

Notice that we've also used the @action decorator to create a custom action, named highlight. This decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.

Custom actions which use the @action decorator will respond to GET requests by default. We can use the methods argument if we wanted an action that responded to POST requests.

The URLs for custom actions by default depend on the method name itself. If you want to change the way url should be constructed, you can include url_path as a decorator keyword argument.


- using routers

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]


# read below for more advance learning
- serializer and viewset api guide
https://www.django-rest-framework.org/api-guide/serializers/



# API Guide 
- serializer
- view
- viewset
- authentication and permissions
- serializer_fields

# other 
https://www.cdrf.co/

# serializer Fields
# core arguments
required - Defaults to True. If you're using Model Serializer default value will be False if you have specified blank=True or default or null=True at your field in your Model.

# paginate request data
def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# General
- write_only, read_only field - incorrect one make error which is deficult to track and debug. so just try changing key. (Caution)
- CSRF validation will only apply to any session authenticated views
- we can add extra data which we want to show in frontend in api response, we can add it in to_representation(), we can also override data that we are showing by default, in to_representation()


# DRF Fields
source - Defaults to the name of the field.


from rest_framework import serializers

class MySerializer(serializers.Serializer):
    my_field = serializers.CharField(initial="initial_value")

    def to_representation(self, instance):
        initial_value = self.fields["my_field"].initial
        # Now, 'initial_value' contains the value set in the 'initial' argument

        # Your remaining to_representation logic here
        # ...

        return representation
    

Remember that the to_representation method is called when converting the serializer data to a representation that can be rendered, such as when serializing data for a response. If you need to access the initial value during the validation or deserialization process, you might use to_internal_value instead.



style
A dictionary of key-value pairs that can be used to control how renderers should render the field.

Two examples here are 'input_type' and 'base_template':

# Use <input type="password"> for the input.
password = serializers.CharField(
    style={'input_type': 'password'}
)

# Use a radio input instead of a select input.
color_channel = serializers.ChoiceField(
    choices=['red', 'green', 'blue'],
    style={'base_template': 'radio.html'}
)


Boolean field - blank kwarg removed, default required=True


+ Writable nested serializers - By default nested serializers are read-only. If you want to support write-operations to a nested serializer field you'll need to create create() and/or update() methods in order to explicitly specify how the child relationships should be saved:


# best Reference Material
cdrf.co

