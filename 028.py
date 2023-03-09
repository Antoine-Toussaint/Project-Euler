import _utilities


@_utilities.benchmark
def solve():
    n = 500
    i = 1
    circle = 0
    som = 1
    for _ in range(n):
        for __ in range(4):
            i += 2*(circle+1)
            som += i
        circle += 1

    return som


if __name__ == '__main__':
    solve()
