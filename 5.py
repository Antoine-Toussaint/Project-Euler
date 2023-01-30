from functools import reduce
from operator import mul


def union(s0, s1):
    s = s0.copy()
    for k1, v1 in s1.items():
        s[k1] = max(v1, s0.get(k1, 0))
    return s


def prime_factors(n):
    s = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            s[i] = s.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        s[n] = 1
    return s


def solve():
    factors = reduce(union, [prime_factors(i) for i in range(2, 21)], {})
    return reduce(mul, [k ** v for k, v in factors.items()])


if __name__ == "__main__":
    print(solve())
