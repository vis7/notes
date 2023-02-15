# Making Queries

- example
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


Model.objects.<below_method>

all()

filter() - Returns a new QuerySet containing objects that match the given lookup parameters.
eg. Entry.objects.filter(pub_date__year=2006)
filter(pub_date__gte=datetime.date(2005, 1, 30))


exclude() - Returns a new QuerySet containing objects that do not match the given lookup parameters.


Each time you refine a QuerySet, you get a brand-new QuerySet that is in no way bound to the previous QuerySet. Each refinement creates a separate and distinct QuerySet that can be stored, used and reused.

QuerySets are lazy – the act of creating a QuerySet doesn’t involve any database activity. You can stack filters together all day long, and Django won’t actually run the query until the QuerySet is evaluated

Retrieving a single object with get()

- limiting queryset
eg. Entry.objects.all()[5:10]

- order_by
Entry.objects.order_by('headline')[0]

# Field lookups
Basic lookups keyword arguments take the form field__lookuptype=value. (That’s a double-underscore). For example:
>>> Entry.objects.filter(pub_date__lte='2006-01-01')

The field specified in a lookup has to be the name of a model field. There’s one exception though, in case of a ForeignKey you can specify the field name suffixed with _id. In this case, the value parameter is expected to contain the raw value of the foreign model’s primary key. For example:

>>> Entry.objects.filter(blog_id=4)

- exact
An “exact” match. For example:

>>> Entry.objects.get(headline__exact="Cat bites dog")

If you don’t provide a lookup type – that is, if your keyword argument doesn’t contain a double underscore – the lookup type is assumed to be exact.

>>> Blog.objects.get(id__exact=14)  # Explicit form
>>> Blog.objects.get(id=14)         # __exact is implied

iexact - A case-insensitive match


contains - Case-sensitive containment test. 

icontains - case-insensitive version of contains

starts_with - Starts-with and ends-with search, respectively.

ends_with - 

in
istarts_with
iends_with
gt
gte
lt
lte
range
date
isnull

regex
iregex

- aggregate function
Avg
Count
Max
Min
StdDev
Sum
Variance



# Lookups that span relationships
 To span a relationship, use the field name of related fields across models, separated by double underscores, until you get to the field you want
Entry.objects.filter(blog__name='Beatles Blog')

This spanning can be as deep as you’d like.

It works backwards, too.

This example retrieves all Blog objects which have at least one Entry whose headline contains 'Lennon':

>>> Blog.objects.filter(entry__headline__contains='Lennon')

__isnull

if you want to compare the value of a model field with another field on the same model you can use F

For example, to find a list of all blog entries that have had more comments than pingbacks, we construct an F() object to reference the pingback count, and use that F() object in the query:

>>> from django.db.models import F
>>> Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))

Django supports the use of addition, subtraction, multiplication, division, modulo, and power arithmetic with F() objects, both with constants and with other F() objects.

The F() objects support bitwise operations by .bitand(), .bitor(), .bitxor(), .bitrightshift(), and .bitleftshift(). For example:


# Get blogs entries with id 1, 4 and 7
>>> Blog.objects.filter(pk__in=[1,4,7])

The field lookups that equate to LIKE SQL statements (iexact, contains, icontains, startswith, istartswith, endswith and iendswith) will automatically escape the two special characters used in LIKE statements – the percent sign and the underscore.

# Complex lookups with Q objects
A Q object (django.db.models.Q) is an object used to encapsulate a collection of keyword arguments.

Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)

SELECT * from polls WHERE question LIKE 'Who%'
    AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')



