import _utilities


def power_sum(n):
    l = [int(d) for d in str(n)]
    return sum([i**5 for i in l])


def is_valid(n):
    return power_sum(n) == n


@_utilities.benchmark
def solve():
    som = 0
    for i in range(2, 1000000):
        som += i*is_valid(i)
    return som


if __name__ == '__main__':
    solve()
