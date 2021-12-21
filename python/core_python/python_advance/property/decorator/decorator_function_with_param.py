'''
This program decorate function with parameters
Smart division
'''

def division(a, b):
    return a/b

def smart_division(func):
    def inner(a, b):
        print(f"dividing {a} by {b}")
        if b == 0:
            print('can not divide by zero')
            return 
        return func(a,b)
    return inner

a = 20
b = 10 # 0

# running function
print("normal division")
print(division(a,b)) # this can not divide by 0

print("\ndivision after making function smart")
division = smart_division(division)
print(division(a,b))
