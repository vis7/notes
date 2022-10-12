# collection
- namedtuple() - factory function for creating tuple subclasses with named fields. The need for this feature arose because using indices to access the values in a regular tuple is annoying, difficult to read, and error-prone. This is especially true if the tuple you’re working with has several items and is constructed far away from where you’re using it.
- deque - list-like container with fast appends and pops on either end
- ChainMap - A dictionary-like class that allows treating a number of mappings as a single dictionary object
- Counter - A dictionary subclass that supports convenient counting of unique items in a sequence or iterable
- OrderedDict - dict subclass that remembers the order entries were added
- defaultdict - dict subclass that calls a factory function to supply missing values
- UserDict - wrapper around dictionary objects for easier dict subclassing
- UserList - wrapper around list objects for easier list subclassing
- UserString - wrapper around string objects for easier string subclassing


Being hashable means that your objects must have a hash value that never changes during their lifetime. This is a requirement because these objects will work as dictionary keys. In Python, immutable objects are also hashable.


https://realpython.com/python-collections-module/
https://www.geeksforgeeks.org/python-collections-module/

# Counter
- elements() - Return an iterator over elements repeating each as many times as its count.
- most_common([n]) - Return a list of the n most common elements and their counts from the most common to the least.
- subtract([iterable-or-mapping]) - Elements are subtracted from an iterable or from another mapping (or counter)
```
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```

- total() - Compute the sum of the counts.
```
c = Counter(a=10, b=5, c=0)
c.total()
15
```

- update([iterable-or-mapping])
Elements are counted from an iterable or added-in from another mapping (or counter). Like dict.update() but adds counts instead of replacing them. Also, the iterable is expected to be a sequence of elements, not a sequence of (key, value) pairs.


# deque
- append(x) - Add x to the right side of the deque.
- appendleft(x) - Add x to the left side of the deque.
- clear() - Remove all elements from the deque leaving it with length 0.
- copy() - Create a shallow copy of the deque.
- count(x) - Count the number of deque elements equal to x.
- extend(iterable) - Extend the right side of the deque by appending elements from the iterable argument.
- extendleft(iterable) - Extend the left side of the deque by appending elements from iterable. Note, the series of left - appends results in reversing the order of elements in the iterable argument.
- index(x[, start[, stop]]) - Return the position of x in the deque (at or after index start and before index stop). - Returns the first match or raises ValueError if not found.
- insert(i, x) - Insert x into the deque at position i.
- pop() - Remove and return an element from the right side of the deque.
- popleft() - Remove and return an element from the left side of the deque.
- remove(value) - Remove the first occurrence of value.
- reverse() - Reverse the elements of the deque in-place and then return None.
- rotate(n=1) - Rotate the deque n steps to the right. If n is negative, rotate to the left.
- maxlen() - Maximum size of a deque or None if unbounded.