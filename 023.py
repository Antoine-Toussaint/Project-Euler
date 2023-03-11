import _utilities


def abundant(n):
    return [i for i in range(2, n) if sum(_utilities.divisors(i)) - i > i]


@_utilities.benchmark
def solve():
    ab = abundant(28123)
    d = set()
    for i in range(0, len(ab)):
        for j in range(i, len(ab)):
            som = ab[i] + ab[j]
            if som < 28123:
                d.add(som)

    return (28122 * 28123) // 2 - sum(d)


if __name__ == '__main__':
    solve()

# not 4190404
