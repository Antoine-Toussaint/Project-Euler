import _utilities


def rotation(l, k):
    n = len(l)
    newl = []
    for i in range(n):
        newl.append(l[(k+i) % n])
    return newl


@_utilities.benchmark
def solve():
    import _utilities

    count = 0
    for i in range(2, 1000000):
        l = _utilities.digits(i)
        is_circular = True
        for k in range(len(l)):
            to_test = int(''.join([str(d) for d in rotation(l, k)]))
            if not _utilities.is_prime(to_test):
                is_circular = False
                break
        if is_circular:
            count += 1
    return count


if __name__ == '__main__':
    solve()
