# ORM
filter
exclude
all 

- we can call update method on above to update multiple records simulteneously

# Field lookup
__ 
- span relationship - foreign key, one to one, 
- other filters ()
    - lte
    - exact
    - iexact
    - contains
    - icontains
    - startswith
    - endswith
    - istartswith
    - iendswith
    - isnull

- based upon the field
    - date element
    - json field element

query_set[start:stop:step] - can be used to slice queryset

- Further filtering or ordering of a sliced queryset is prohibited due to the ambiguous nature of how that might work.



get



accecssing attirbute form object using obj.<Model>_set
accecssing attribute in filter <foreign_key_field_name>__<attribute of that field>

can chain multiple queries together that will evaluate when object called due to lazy loading


# Q
Q can be used to combine multiple condition
| - OR
& - AND
~ - NOT
^ - XOR

# F
F used to get the value of the column for comparision. we can do arithmatic operations on field in F
The F() objects support bitwise operations by .bitand(), .bitor(), .bitxor(), .bitrightshift(), and .bitleftshift(). For example:
>>> F('somefield').bitand(16)

- many to many relationship special methods
add
create
remove
clear
set

JSONField methods
contains - The returned objects are those where the given dict of key-value pairs are all contained in the top-level of the field.
contained_by - This is the inverse of the contains lookup - the objects returned will be those where the key-value pairs on the object are a subset of those in the value passed. For example:

has_key
has_keys
has_any_keys


# annotation and aggregation



