import _utilities


def divide(n, steps):
    l = []
    val = 1
    for _ in range(steps):
        div = val//n
        val -= div*n
        l.append(div)
        val *= 10
    return l


def cycle(n):
    d = divide(n, 5000)
    while d[0] == 0:
        d.remove(0)
    for offset in range(2500):
        for length in range(1, 1000):
            is_cycle = True
            pattern = d[offset:offset+length]
            current_offset = offset+2*length
            while current_offset + length < 5000:
                if d[current_offset:current_offset+length] != pattern:
                    is_cycle = False
                    break
                current_offset += length
            if is_cycle:
                return length


@_utilities.benchmark
def solve():
    c_max = 0
    n_max = 0
    for i in range(3, 1000):
        c = cycle(i)
        if c > c_max:
            c_max = c
            n_max = i
    return n_max


if __name__ == '__main__':
    solve()
