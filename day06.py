L = open("day06.txt").readline()
n = 4
while True:
    if len(set(L[n - 4 : n])) == 4:
        print(f"Part 1: {n}")
        break
    else:
        n += 1

n = 14
while True:
    if len(set(L[n - 14 : n])) == 14:
        print(f"Part 2: {n}")
        break
    else:
        n += 1
