import _utilities


@_utilities.benchmark
def solve():
    import _utilities

    non_trivial_fractions = []
    for d in range(10, 100):
        for n in range(10, d):
            for i in range(1, 10):
                for j in range(1, i):
                    if i*n == d*j:
                        ln = _utilities.digits(n)
                        ld = _utilities.digits(d)
                        if not i in ld or not j in ln:
                            continue
                        ld.remove(i)
                        ln.remove(j)
                        if ln == ld and ln != [0]:
                            non_trivial_fractions.append((j, i))

    nums, dens = [i for i, j in non_trivial_fractions], [
        j for i, j in non_trivial_fractions]
    return _utilities.simplify_fraction(_utilities.prod(nums), _utilities.prod(dens))[1]


if __name__ == '__main__':
    solve()
