import _utilities


@_utilities.benchmark
def solve():
    terms_primes_fact = []
    for a in range(2, 101):
        for b in range(2, 101):
            f = _utilities.prime_factorization(a)
            f *= b
            f = sorted(f)
            if not f in terms_primes_fact:
                terms_primes_fact.append(f)
    return len(terms_primes_fact)


if __name__ == '__main__':
    solve()
