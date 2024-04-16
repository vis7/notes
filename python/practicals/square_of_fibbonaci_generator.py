# create square of fibbonacii sequance using chaning generator
def fibbonacii_sequence(n):
    x, y = 0, 1
    i = 0
    while i < n:
        x, y = y, y+x
        yield x
        i += 1

def square_numbers(nums):
    for num in nums:
        yield num * num

print(sum(square_numbers(fibbonacii_sequence(10))))


