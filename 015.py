import _utilities
from math import factorial


@_utilities.benchmark
def solve():
    n = 20
    return factorial(2*n)//(factorial(n)**2)


if __name__ == "__main__":
    solve()
