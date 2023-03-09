import _utilities


@_utilities.benchmark
def solve():
    import math
    import _utilities

    som = 0
    for i in range(3, 1000000):
        l = _utilities.digits(i)
        if sum([math.factorial(d) for d in l]) == i:
            som += i

    return som


if __name__ == '__main__':
    solve()
