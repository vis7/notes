def power_two_gen():
    n = 0
    while True:
        yield n ** 2
        n += 1

itr = power_two_gen()

# results
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
