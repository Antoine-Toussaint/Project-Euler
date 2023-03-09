import _utilities


@_utilities.benchmark
def solve():
    n = 1000
    u = 2 ** 0
    for _ in range(n):
        u *= 2
        while u % 10 == 0:
            u //= 10
    return sum([int(el) for el in str(u)])


if __name__ == '__main__':
    solve()
