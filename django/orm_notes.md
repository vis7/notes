# ORM
- filter()
- exclude()
- all() 
- get()
- order_by()

We can call update method on above to update multiple records simulteneously

# Aggregate Function
- Avg
- Count
- Max
- Min
- StdDev
- Sum
- Variance


# Field lookup "__"
- span relationship - foreign key, one to one, 
- other filters ()
    - in
    - exact
    - iexact
    - contains
    - icontains
    - startswith
    - endswith
    - istartswith
    - iendswith
    - isnull
    - gt
    - gte
    - lt
    - lte
    - range
    - date
    - isnull
    - regex
    - iregex


- based upon the field
    - date element
    - json field element

query_set[start:stop:step] - can be used to slice queryset

Further filtering or ordering of a sliced queryset is prohibited due to the ambiguous nature of how that might work.



## get
accecssing attirbute form object using obj.<Model>_set
accecssing attribute in filter <foreign_key_field_name>__<attribute of that field>

can chain multiple queries together that will evaluate when object called due to lazy loading

# Q
Q can be used to combine multiple condition
```
| - OR
& - AND
~ - NOT
^ - XOR
```
# F
if you want to compare the value of a model field with another field on the same model you can use F. F used to get the value of the column for comparision. we can do arithmatic operations on field in F

Django supports the use of addition, subtraction, multiplication, division, modulo, and power arithmetic with F() objects, both with constants and with other F() objects.

The F() objects support bitwise operations by .bitand(), .bitor(), .bitxor(), .bitrightshift(), and .bitleftshift(). For example:
```
>>> F('somefield').bitand(16)
```

Many to many relationship special methods
- add
- create
- remove
- clear
- set

JSONField methods

- contains - The returned objects are those where the given dict of key-value pairs are all contained in the top-level of the field.
- contained_by - This is the inverse of the contains lookup - the objects returned will be those where the key-value pairs on the object are a subset of those in the value passed. For example:
- has_key
- has_keys
- has_any_keys


# annotation and aggregation


Each time you refine a QuerySet, you get a brand-new QuerySet that is in no way bound to the previous QuerySet. QuerySets are lazy – the act of creating a QuerySet doesn’t involve any database activity. You can stack filters together all day long, and Django won’t actually run the query until the QuerySet is evaluated


# some good things to know
The field specified in a lookup has to be the name of a model field. There’s one exception though, in case of a ForeignKey you can specify the field name suffixed with _id.
```
>>> Entry.objects.filter(blog_id=4)
```

If you don’t provide a lookup type – that is, if your keyword argument doesn’t contain a double underscore – the lookup type is assumed to be exact.
```
>>> Blog.objects.get(id__exact=14)  # Explicit form
>>> Blog.objects.get(id=14)         # __exact is implied
```
The field lookups that equate to LIKE SQL statements (iexact, contains, icontains, startswith, istartswith, endswith and iendswith) will automatically escape the two special characters used in LIKE statements – the percent sign and the underscore.

the display value for a field with choices can be accessed using the get_FOO_display() method. For example:
```
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
```

The primary key field is read-only. If you change the value of the primary key on an existing object and then save it, a new object will be created alongside the old one

# some examples
```
Entry.objects.get(title__regex=r"^(An?|The) +")
```

This example retrieves all Blog objects which have at least one Entry whose headline contains 'Lennon':
```
>>> Blog.objects.filter(entry__headline__contains='Lennon')
```

For example, to find a list of all blog entries that have had more comments than pingbacks, we construct an F() object to reference the pingback count, and use that F() object in the query:
```
>>> from django.db.models import F
>>> Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
```

# Get blogs entries with id 1, 4 and 7
```
>>> Blog.objects.filter(pk__in=[1,4,7])
```

```
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)

SELECT * from polls WHERE question LIKE 'Who%'
    AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
```
