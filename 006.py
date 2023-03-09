import _utilities


def sum_ind_sq(n):
    return n * (n + 1) * (2 * n + 1) // 6


@_utilities.benchmark
def solve():
    n = 100
    s = n * (n + 1) // 2
    return s*s - sum_ind_sq(n)


if __name__ == '__main__':
    solve()
