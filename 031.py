import _utilities

possible_values = [200, 100, 50, 20, 10, 5, 2, 1]


def solve_aux(target, max):
    global possible_values

    sols = []
    for p in possible_values:
        if p > max:
            continue
        if p == target:
            sols.append([p])
        if p < target:
            other_sols = solve_aux(target-p, p)
            for s in other_sols:
                sols.append([p] + s)

    return len(sols)


@_utilities.benchmark
def solve():
    return solve_aux(200, 1000)


if __name__ == '__main__':
    solve()
