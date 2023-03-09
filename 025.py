import _utilities


@_utilities.benchmark
def solve():
    f1 = 1
    f2 = 1
    u = 2
    while len(str(f2)) < 1000:
        f1, f2 = f2, f1+f2
        u += 1
    return u


if __name__ == '__main__':
    solve()
