- to remove all migrations # use powershell
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Learn
orm
signals
middleware
cache


celery
rabbitmq
stripe


# notes
- User is able to login only if it is active
- form_valid method is overridden in view rather then form