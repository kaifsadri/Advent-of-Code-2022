L = list(line.strip() for line in open("day03.txt", "r").readlines())
P = dict(
    zip(
        "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper(),
        range(1, 53),
    )
)

S = 0
for bp in L:
    r, l = set(bp[: len(bp) // 2]), set(bp[len(bp) // 2 :])
    com = set.intersection(r, l).pop()
    S += P[com]
print(f"Part 1: {S}")

S = 0
for g in range(len(L) // 3):
    e1, e2, e3 = map(set, L[g * 3 : g * 3 + 3])
    com = set.intersection(e1, e2, e3).pop()
    S += P[com]
print(f"Part 2: {S}")
