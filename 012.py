import _utilities
from math import sqrt


@_utilities.benchmark
def solve():
    n = 500
    s, i = 1, 2
    while True:
        s, i = s+i, i+1
        c = 0
        for k in range(1, int(sqrt(s))+1):
            if s % k == 0:
                c += 1
        if c > (n/2):
            return s


if __name__ == '__main__':
    solve()
