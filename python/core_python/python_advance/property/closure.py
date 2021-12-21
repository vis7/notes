'''
this program illustrate use of closure
making multiplier of any number using clouser
'''

def make_muliplier(n):
    def inner(x):
        return n*x
    return inner

time5 = make_muliplier(5)
print(time5(3))

time6 = make_muliplier(6)
print(time6(3))
