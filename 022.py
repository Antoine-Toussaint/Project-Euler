import _utilities


@_utilities.benchmark
def solve():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open('022_names.txt') as f:
        d = f.read()
        index, names, d_len = 1, [], len(d)
        new_name = ''
        while index < d_len:
            if d[index] == '\"':
                names.append(new_name)
                new_name = ""
                index += 3
            else:
                new_name += d[index]
                index += 1
        names = sorted(names)
        l = []
        for i in range(len(names)):
            score = 0
            for letter in names[i]:
                score += alphabet.index(letter) + 1
            score *= i+1
            l.append(score)

        return sum(l)


if __name__ == '__main__':
    solve()
