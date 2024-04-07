def smart_division(func):
    def inner(a, b):
        # custom logic
        if b == 0:
            print("Can not divide by zero")
            return 0

        return func(a, b)

    return inner

@smart_division
def div(a, b):
    return a/b


print("Before decorating")
# print(div(25,0)) # will produce error


print("\n\nAfter decorating")
# div = smart_division(div)
print(div(25,0))


