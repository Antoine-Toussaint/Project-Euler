import _utilities


@_utilities.benchmark
def solve():
    primes = [2]
    candidate = 3
    while candidate < 2000000:
        is_prime = True
        sqrt = candidate ** 0.5
        for prime in primes:
            if prime > sqrt:
                break
            elif candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    return sum(primes)


if __name__ == '__main__':
    solve()
