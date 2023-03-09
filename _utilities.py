max_tested = 2
primes = [2]


def benchmark(func):
    """
    Decorator to benchmark a function.
    """

    import time
    import inspect

    day = inspect.getfile(func).split('\\')[-1].split('.')[0]
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
            n /= p
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
