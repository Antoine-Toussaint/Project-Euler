import _utilities


@_utilities.benchmark
def solve():
    answer, i, j = 0, 1, 1

    while i < 4000000:
        if not (i % 2):
            answer += i
        i, j = j, i+j

    return answer


if __name__ == '__main__':
    solve()
