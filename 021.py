from math import sqrt
import _utilities


def divisors(n):
    yield 1
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            yield i
            yield n // i


@_utilities.benchmark
def solve():
    n = 10000
    l = []
    ds = [sum(divisors(i)) for i in range(n)]
    for i in range(n):
        if ds[i] < n and ds[i] != i and i == ds[ds[i]]:
            l.append(i)
    return sum(l)


if __name__ == '__main__':
    solve()
