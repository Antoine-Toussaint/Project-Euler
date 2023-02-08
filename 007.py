def solve():
    n = 10001
    primes = [2]
    candidate = 3
    while len(primes) < n:
        for p in primes:
            if candidate % p == 0:
                break
        else:
            primes.append(candidate)
        candidate += 2
    return primes[-1]


if __name__ == "__main__":
    print(solve())
