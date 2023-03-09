import _utilities


@_utilities.benchmark
def solve():
    n = 100
    u = 1
    for i in range(1, n+1):
        u *= i
        while u % 10 == 0:
            u //= 10
    return sum([int(el) for el in str(u)])


if __name__ == '__main__':
    solve()
