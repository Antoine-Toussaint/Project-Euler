import _utilities


@_utilities.benchmark
def solve():
    import _utilities

    l = _utilities.primes_to(100000)
    som = 0
    for p in l:
        digits = _utilities.digits(p)
        is_valid = True
        for k in range(1, len(digits)):
            p0 = int(''.join([str(d) for d in digits[0:k]]))
            p1 = int(''.join([str(d) for d in digits[0:k]]))
            if not p0 in l or not p1 in l:
                is_valid = False
                break
        if is_valid:
            som += p


if __name__ == '__main__':
    solve()
