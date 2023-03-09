import _utilities


def abundant(n):
    return [i for i in range(2, n) if sum(_utilities.divisors(i))+1 > i]


def is_sum_of_two(l, n):
    for el in l:
        if n-el in l:
            return True
    return False


@_utilities.benchmark
def solve():
    ab = abundant(28123)
    d = {}
    for a0 in ab:
        for a1 in ab:
            som = a0 + a1
            if som < 28123:
                d[som] = 1

    return sum(list(range(0, 28123))) - sum(list(d.keys()))


if __name__ == '__main__':
    solve()
