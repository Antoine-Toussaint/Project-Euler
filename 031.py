import _utilities

possible_values = [200, 100, 50, 20, 10, 5, 2, 1]


@_utilities.benchmark
def solve(target=200, max=1000):
    global possible_values

    sols = []
    for p in possible_values:
        if p > max:
            continue
        if p == target:
            sols.append([p])
        if p < target:
            other_sols = solve(target-p, p)
            for s in other_sols:
                sols.append([p] + s)

    return len(sols)


if __name__ == '__main__':
    solve()
