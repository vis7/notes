# Basic
Django - https://github.com/codingforentrepreneurs/Try-Django

# DRF
- https://www.django-rest-framework.org/tutorial/1-serialization/
- https://www.django-rest-framework.org/api-guide/serializers/
- https://www.django-rest-framework.org/api-guide/views/
- https://www.django-rest-framework.org/api-guide/viewsets/


oauth
send msgs
drf revision
django and DRF Testing


# advance django topics
cache 
authentication
signals
pagination
middleware
unit test


- how to increase performace of application, how to make application scalable
pre_fetch()


# performance
https://www.netguru.com/blog/django-performance-optimization (sort)
https://www.esparkinfo.com/blog/django-performance-tips.html (in details - get overview and do practicals)
https://docs.djangoproject.com/en/4.1/topics/performance/
https://docs.djangoproject.com/en/4.1/topics/cache/


https://github.com/jazzband/django-silk


# tips
use cache and you should also bear in mind that all static content should be served by an HTTP cache server.

Django sessions settings in order to process requests faster. Instead of storing user sessions in a slow database, which is the default mode in Django, you would be better off storing session data in memory. Just use the command “SESSION_ENGINE = ‘django.contrib.sessions.backends.cache” and relish in the improved performance that your app will get from a cached-based session backend.

use
select_related() - “this is a performance booster which results in a single, more complex, query” - utilizing it also means that the later use of any foreign-key relationships won’t require database queries;

prefetch_related() - this allows users to prefetch many-to-many and many-to-one objects and, as a result, improves the performance of the entire framework.

@cached_property - The @cached_property decorator caches the result of a method with a single self argument as a property. The cached result will persist as long as the instance does, so if the instance is passed around and the function subsequently invoked, the cached result will be returned.


Use performance booster to to handle big number of requests

# Questions
- RequestFactory vs Client for testing (DRF - APIRequestFactory and RequestFactory)
https://stackoverflow.com/questions/30992377/django-test-requestfactory-vs-client



# add ons
linter
auto pep8 code corrections
