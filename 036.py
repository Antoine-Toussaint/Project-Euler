import _utilities


def is_palyndrome(l):
    n = len(l)//2
    for i in range(n):
        if l[i] != l[-(i+1)]:
            return False
    return True


def to_binary(n):
    l = []
    while n != 0:
        l.append(n % 2)
        n //= 2
    l.reverse()
    return l


@_utilities.benchmark
def solve():
    import _utilities

    som = 0
    for i in range(1000000):
        if is_palyndrome(_utilities.digits(i)) and is_palyndrome(to_binary(i)):
            som += i
    return som


if __name__ == '__main__':
    solve()
