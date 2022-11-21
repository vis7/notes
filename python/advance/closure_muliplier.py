def multiplier_of(m):
    def multiplier(n):
        return m*n
    return multiplier

time5 = multiplier_of(5)
time3 = multiplier_of(3)


print(time5(20))
print(time3(10))
print(time3(time5(10)))
