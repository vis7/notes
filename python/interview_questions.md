string, list, set, dict methods
builtin python methods


which oop is not supported by python (python oop)
dictionary key must be hashble (int, str, tuple)



# Practicals
```
nums = [1, 9, 4, 12, 20, 2, 8, 21, 3] 
# output = : 1, 4, 2, 3, 

nums = [36, 60, 32, 70, 35, 63, 34, 33] 
# output : 36 32 35 34 33 
```

```
#Get the longest starting string match in the list. 

nums = [“flower”, “flow”, “flight”] 
# output = “fl” 
```

```
# Let us know the output: 

squares = [] 
for x in range(50): 
    squares.append(lambda: x**3) 

print(squares[25]()) 
print(squares[5]())
```


# reverse string without using built in function or slicing
mystr = "parshv"
new_string = ""
for i in range(len(mystr)-1, -1, -1):
    new_string += mystr[i]

# produce below output from input using list comprehention
input = ["a1", "b2b", "cc3c", 4, 5, 6.5, "7.5"]
output = ["a1 String", "b2b String", "cc3c String", "4 Digit", "5 Digit", "6.5 Digit", "7.5 Digit"]


[f"{i} Stirng" if type(i).__name__ == 'str' else f"{i} Digit" for i in input]



find missing element in inputs = [4, 2, 3, 6]


minion game