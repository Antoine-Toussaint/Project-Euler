import _utilities


def is_max(perm, offset):
    m = True
    i = perm[-1]
    for k in range(-2, -(offset+1), -1):
        if perm[k] < i:
            m = False
            break
        i = perm[k]
    return m


def next(perm, offset=None, recursed_call=False):
    if offset == None:
        offset = len(perm)
    if not recursed_call:
        self_is_max = is_max(perm, offset)
    else:
        self_is_max = False

    if not self_is_max:
        if is_max(perm, offset-1):
            vals = perm[-1:-(offset+1):-1]
            vals.sort()
            for el in vals:
                if el > perm[-offset]:
                    start_val = el
                    break
            vals.remove(start_val)
            return perm[0:len(perm)-offset] + [start_val] + vals
        else:
            return next(perm, offset-1, True)


@_utilities.benchmark
def solve():
    start = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1000000):
        start = next(start)
    return start


if __name__ == '__main__':
    solve()
