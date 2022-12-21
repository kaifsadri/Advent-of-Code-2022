from collections import deque

L = open("day20.txt").read().strip().split("\n")
e = 0.001

O = list()
for line in L:
    # there is a trick here. The puzzle input has duplicate items here.
    # We add noise to make them unique. The noise is then removed by rounding.
    i = float(line)
    while i in O:
        if i > 0:
            i += e
        if i < 0:
            i -= e
    O.append(i)
D = deque(O)
for num in O:
    n = D.index(num)
    D.rotate(-n)
    D.popleft()
    D.rotate(-int(num))
    D.appendleft(num)
n = D.index(0)
D.rotate(-n)
print(f"Part 1: {sum(int(D[i % len(D)]) for i in [1000, 2000, 3000])}")

O = list()
for line in L:
    i = float(line) * 811589153
    while i in O:
        if i > 0:
            i += e
        if i < 0:
            i -= e
    O.append(i)
D = deque(O)
for r in range(10):
    for num in O:
        n = D.index(num)
        D.rotate(-n)
        D.popleft()
        D.rotate(-int(num))
        D.appendleft(num)
n = D.index(0)
D.rotate(-n)
print(f"Part 2: {sum(int(D[i % len(D)]) for i in [1000, 2000, 3000])}")
