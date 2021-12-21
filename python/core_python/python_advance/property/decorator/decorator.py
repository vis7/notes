'''
This program contain implimentation of decorator
'''

def ordinary():
    print('I am ordinary function')

def make_pretty(func):
    def inner():
        print('making function prettier')
        func()
    return inner

print('normal ordinary function')
ordinary()

print('\nfunction after making it pretty')
ordinary = make_pretty(ordinary)
ordinary()

