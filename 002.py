answer, i, j = 0, 1, 1

while i < 4000000:
    if not (i % 2):
        answer += i
    i, j = j, i+j

print(answer)
