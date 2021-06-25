import math


def f1(x):
    return x * x * x


def f2(x):
    return math.log2(x)


def f3(x):
    return x * math.log2(x)


def f4(x):
    return (3 / 2) ** x


def f5(x):
    if math.log2(x) == 0:
        return None
    return x / (math.log2(x))


def f6(x):
    return 2 ** x


def f7(x):
    return math.sqrt(x)


def f8(x):
    if math.log2(x) <= 0:
        return None
    return math.log2(math.log2(x))


def f9(x):
    return x ** 2


def f10(x):
    return x


def f11(x):
    return (math.log2(x)) ** 2


def f12(x):
    return (1 / 3) ** x
