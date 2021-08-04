from functools import partial


'''
    Initially I thought to use ready-made operators from the operator module, 
    but I needed to use keyword arguments in operator functions, 
    and functions from operator do not provide such possibilities, so I wrote my own functions.
'''

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def floordiv(a, b):
    return a // b


def mul(a, b):
    return a * b


def zero(func=None):
    if func:
        return func(0)
    return 0


def one(func=None):
    if func:
        return func(1)
    return 1


def two(func=None):
    if func:
        return func(2)
    return 2


def three(func=None):
    if func:
        return func(3)
    return 3


def four(func=None):
    if func:
        return func(4)
    return 4


def five(func=None):
    if func:
        return func(5)
    return 5


def six(func=None):
    if func:
        return func(6)
    return 6


def seven(func=None):
    if func:
        return func(7)
    return 7


def eight(func=None):
    if func:
        return func(8)
    return 8


def nine(func=None):
    if func:
        return func(9)
    return 9


def plus(n):
    return partial(add, b=n)


def minus(n):
    return partial(sub, b=n)


def times(n):
    return partial(mul, b=n)


def divided_by(n):
    return partial(floordiv, b=n)
