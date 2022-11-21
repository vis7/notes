def power_two_gen():
    n = 0
    while True:
        yield n ** 2
        n += 2

itr = power_two_gen()
