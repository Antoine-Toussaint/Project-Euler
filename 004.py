import math


def reversed_num(n: int):
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = (n - rem) // 10
    return rev


def is_palyndrome(n: int):
    return reversed_num(n) == n


def solve():
    for i in reversed(range(100, 1000)):
        f = float(i)
        limit = math.floor(((f-1) * (f-1))/f)
        for j in reversed(range(max([100, limit]), i+1)):
            if is_palyndrome(i*j):
                return i * j


def naive():
    m = 0
    for i in range(1000):
        for j in range(1000):
            if is_palyndrome(i*j):
                m = max([m, i*j])
    return m


print(solve())
