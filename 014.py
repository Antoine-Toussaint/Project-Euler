import _utilities


@_utilities.benchmark
def solve():
    n = 1000000
    max, max_num = 0, 0
    to_test = [True] * n
    for i in range(2, n):
        count, h = 1, i
        if to_test[h]:
            while h != 1:
                count += 1
                if h < n:
                    to_test[h] = False
                if h % 2 == 0:
                    h //= 2
                else:
                    h = h*3+1
            if count > max:
                max = count
                max_num = i

    return max_num


if __name__ == '__main__':
    solve()
