def infinite_sequence():
    num = 0
    while True:
        yield num * 3
        num += 3

iterator = infinite_sequence()
print(next(iterator))
print(next(iterator))
print(next(iterator))


for i in infinite_sequence():
    print(i, end=' ')
    if i > 5:
        break