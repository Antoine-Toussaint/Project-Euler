import _utilities

under_twenty_lengths = [3, 3, 5, 4, 4, 3,
                        5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
dozens_lengths = [6, 6, 5, 5, 5, 7, 6, 6]


def length_num(n):
    l = 0
    if n == 1000:
        return 11
    if (n//100) > 0:
        l += 7 + under_twenty_lengths[n//100-1]
        if (n % 100) > 0:
            l += 3
    if (n % 100) > 19:
        l += dozens_lengths[(n % 100)//10-2]
        if n % 10 != 0:
            l += under_twenty_lengths[n % 10-1]
    elif (n % 100) > 0:
        l += under_twenty_lengths[(n % 100)-1]

    return l


@_utilities.benchmark
def solve():
    n = 1000
    return sum([length_num(i) for i in range(1, n+1)])


if __name__ == '__main__':
    solve()
