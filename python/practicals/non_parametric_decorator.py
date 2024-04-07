# decorator function
def make_pretty(func):
    def inner():
        # our custom logic
        print("Making function pretty")
        func()

    return inner


def ordinary():
    print("I am ordinary function")

# calling simply
print("Before decorating")
ordinary()



# calling after decorating it
print("\n\n\nAfter decorating")
ordinary = make_pretty(ordinary)
ordinary()
