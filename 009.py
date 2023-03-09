import _utilities


def is_triplet(a, b, c):
    return a**2 + b**2 == c**2


@_utilities.benchmark
def solve():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if is_triplet(a, b, c):
                return a * b * c


if __name__ == '__main__':
    solve()
