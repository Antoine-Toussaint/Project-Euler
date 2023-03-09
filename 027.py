from math import sqrt
import _utilities

primes = [2]


def set_primes(n):
    for i in range(primes[-1]+1, n+1):
        is_prime = True
        sr = sqrt(i)
        for p in primes:
            if p > sr:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)


def is_prime(n):
    if primes[-1] < n:
        set_primes(n+1000)
    return n in primes


@_utilities.benchmark
def solve():
    maxscore = 0
    maxscorecouple = (0, 0)
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            i = 0
            while is_prime(i**2 + a*i + b):
                i += 1
            if i > maxscore:
                maxscore = i
                maxscorecouple = (a, b)

    return maxscorecouple[0] * maxscorecouple[1]


if __name__ == '__main__':
    solve()
