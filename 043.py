import _utilities


def next_it(l):
    if l[-1] != 9:
        l[-1] += 1
    else:
        index = 0
        while l[-index] == 9:
            index += 1
        for i in range(1, index+1):
            l[-i] = 0
        try:
            l[-(index+1)] += 1
        except:
            pass


@_utilities.benchmark
def solve():
    l = [0, 0, 0]
    for i in range(101):
        next_it(l)


if __name__ == '__main__':
    solve()
