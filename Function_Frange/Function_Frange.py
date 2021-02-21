def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
for n in frange(1, 10, 0.5):
    print(n)

