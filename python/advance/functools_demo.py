from functools import partial

def power(a, b):
    return a ** b

power3 = partial(power, b=3)
power5 = partial(power, b=5)
power_of_2 = partial(power, 2)

print(power3(2))
print(power5(2))
print(power_of_2(2))

print(power3.func)
print(power3.keywords)
print(power_of_2.args)
