import _utilities


def is_9pandigital(n):
    l = [int(d) for d in str(n)]
    if len(l) != 9:
        return False
    for i in range(1, 10):
        if i not in l:
            return False
    return True


@_utilities.benchmark
def solve():
    d = {}
    for i in range(1, 10000):
        for j in range(10000//i):
            if is_9pandigital(int(str(i) + str(j) + str(i*j))):
                d[i*j] = 1
    return sum(d.keys())


if __name__ == '__main__':
    solve()
