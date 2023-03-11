import platform


max_tested = 2
primes = [2]


separator = "\\" if platform.system() == "Windows" else "/"


def benchmark(func):
    """
    Decorator to benchmark a function.
    """

    import time
    import inspect

    day = inspect.getfile(func).split(separator)[-1].split('.')[0]
    time_length = 20

    def wrapper(*args, **kwargs):
        start = time.time() * 1000
        result = func(*args, **kwargs)
        end = time.time() * 1000
        time_str = f"{end - start:.5f} ms"

        print(f"{day} || {' ' * (time_length - len(time_str))}{time_str} || {result}")
        return result

    return wrapper


def compute_primes_until(n: int):
    global max_tested, primes

    candidate = max_tested + 1
    while candidate < n:
        is_prime = True
        for p in primes:
            if not (candidate % p):
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    max_tested = candidate


def prime_factorization(n: int):
    dividers = []
    prime_index = 0
    while n != 1:
        if prime_index == len(primes):
            compute_primes_until(primes[-1] + 200)
        p = primes[prime_index]
        while not (n % p):
            n //= p
            dividers.append(p)
        prime_index += 1

    return dividers


def reversed_num(n: int):
    """
    Reverses the digits order of the input.
    """

    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = (n - rem) // 10
    return rev


def is_palyndrome(n: int):
    return reversed_num(n) == n


def digits(n):
    return [int(d) for d in str(n)]


def primes_to(n):
    """
    @return: a list of primes from 0 to n included (sorted)
    """

    if n > max_tested:
        compute_primes_until(n)

    ps = []
    for p in primes:
        if p > n:
            break
        ps.append(p)

    return ps


def divisors(n):
    """
    @return: a list of all divisors of n (unsorted)
    """
    import math

    if n < 3:
        return []

    div = [1]
    rn = math.sqrt(n)
    limit = math.ceil(rn)
    for i in range(2, limit):
        if n % i == 0:
            div.append(i)
            div.append(n//i)
    if limit * limit == 0:
        div.append(limit)

    div.append(n)

    return div


def prod(l):
    p = 1
    for el in l:
        p *= el
    return p


def simplify_fraction(n, d):
    pdn = prime_factorization(n)
    pdd = prime_factorization(d)
    common_div = []
    for d in pdn:
        if d in pdd:
            pdd.remove(d)
            common_div.append(d)
    for d in common_div:
        pdn.remove(d)
    return (prod(pdn), prod(pdd))


def is_prime(n):
    import math
    global primes

    if n == 2 or n == 3:
        return True
    if n == 1 or n == 0:
        return False

    rn = math.ceil(math.sqrt(n))
    if primes[-1] < rn:
        compute_primes_until(rn+100)

    for p in primes:
        if p > rn:
            return True
        if n % p == 0:
            return False
