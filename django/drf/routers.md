This means you'll need to explicitly set the basename argument when registering the viewset, or need to specify `queryset` attribute in viewset.

# Authentication
The authentication schemes are always defined as a list of classes. REST framework will attempt to authenticate with each class in the list, and will set request.user and request.auth using the return value of the first class that successfully authenticates.

If no class authenticates, request.user will be set to an instance of django.contrib.auth.models.AnonymousUser, and request.auth will be set to None.

