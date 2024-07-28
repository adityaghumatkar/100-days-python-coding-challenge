def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1, 2, 3, 4, 5, 6, 7)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    print(n)

calculate(2, add=3, multiply=5 )