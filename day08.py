from math import prod

L = list(line.strip() for line in open("day08.txt").readlines())
G = dict()
for row, line in enumerate(L):
    for col, t in enumerate(line):
        G[(row, col)] = int(t)
S = len(L)
V = set()
for row in range(S):
    # looking right
    max_h = -1
    for col in range(S):
        if max_h == 9:
            break
        if (h := G[(row, col)]) > max_h:  # found one
            V.add((row, col))
            max_h = h
    # looking left
    max_h = -1
    for col in range(S - 1, -1, -1):
        if max_h == 9:
            break
        if (h := G[(row, col)]) > max_h:  # found one
            V.add((row, col))
            max_h = h
for col in range(S):
    # looking down
    max_h = -1
    for row in range(S):
        if max_h == 9:
            break
        if (h := G[(row, col)]) > max_h:  # found one
            V.add((row, col))
            max_h = h
    # looking up
    max_h = -1
    for row in range(S - 1, -1, -1):
        if max_h == 9:
            break
        if (h := G[(row, col)]) > max_h:  # found one
            V.add((row, col))
            max_h = h
print(f"Part 1: {len(V)}")

VD = dict()
for row in range(1, S - 1):
    for col in range(1, S - 1):
        VD[(row, col)] = [0, 0, 0, 0]
        # look left
        for c in range(col - 1, -1, -1):
            if G[(row, c)] >= G[(row, col)] or c == 0:
                VD[(row, col)][0] = col - c
                break
        # look right
        for c in range(col + 1, S):
            if G[(row, c)] >= G[(row, col)] or c == S - 1:
                VD[(row, col)][1] = c - col
                break
        # look up
        for r in range(row - 1, -1, -1):
            if G[(r, col)] >= G[(row, col)] or r == 0:
                VD[(row, col)][2] = row - r
                break
        # look down
        for r in range(row + 1, S):
            if G[(r, col)] >= G[(row, col)] or r == S - 1:
                VD[(row, col)][3] = r - row
                break
print(f"Part 2: {max(prod(k) for k in VD.values())}")
