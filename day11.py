from collections import Counter
from math import prod

M = dict()
M[0] = {
    "items": [98, 97, 98, 55, 56, 72],
    "Ops": lambda x: (x * 13) // 3,
    "Test": lambda x: (x % 11 == 0),
    "Target": (4, 7),
}

M[1] = {
    "items": [73, 99, 55, 54, 88, 50, 55],
    "Ops": lambda x: (x + 4) // 3,
    "Test": lambda x: (x % 17 == 0),
    "Target": (2, 6),
}
M[2] = {
    "items": [67, 98],
    "Ops": lambda x: (x * 11) // 3,
    "Test": lambda x: (x % 5) == 0,
    "Target": (6, 5),
}

M[3] = {
    "items": [82, 91, 92, 53, 99],
    "Ops": lambda x: (x + 8) // 3,
    "Test": lambda x: (x % 13) == 0,
    "Target": (1, 2),
}
M[4] = {
    "items": [52, 62, 94, 96, 52, 87, 53, 60],
    "Ops": lambda x: (x * x) // 3,
    "Test": lambda x: (x % 19) == 0,
    "Target": (3, 1),
}

M[5] = {
    "items": [94, 80, 84, 79],
    "Ops": lambda x: (x + 5) // 3,
    "Test": lambda x: (x % 2) == 0,
    "Target": (7, 0),
}
M[6] = {
    "items": [89],
    "Ops": lambda x: (x + 1) // 3,
    "Test": lambda x: (x % 3) == 0,
    "Target": (0, 5),
}

M[7] = {
    "items": [70, 59, 63],
    "Ops": lambda x: (x + 3) // 3,
    "Test": lambda x: (x % 7) == 0,
    "Target": (4, 3),
}

I = Counter()
for r in range(20):
    for m in range(len(M)):
        I[m] += len(M[m]["items"])
        while M[m]["items"]:
            item = M[m]["items"].pop()
            w = M[m]["Ops"](item)
            if M[m]["Test"](w):
                M[M[m]["Target"][0]]["items"].append(w)
            else:
                M[M[m]["Target"][1]]["items"].append(w)

print(f"Part 1: {prod(k[1] for k in I.most_common(2))}")

M = dict()
M[0] = {
    "items": [98, 97, 98, 55, 56, 72],
    "Ops": lambda x: (x * 13),
    "Test": lambda x: (x % 11 == 0),
    "Target": (4, 7),
}

M[1] = {
    "items": [73, 99, 55, 54, 88, 50, 55],
    "Ops": lambda x: (x + 4),
    "Test": lambda x: (x % 17 == 0),
    "Target": (2, 6),
}
M[2] = {
    "items": [67, 98],
    "Ops": lambda x: (x * 11),
    "Test": lambda x: (x % 5) == 0,
    "Target": (6, 5),
}

M[3] = {
    "items": [82, 91, 92, 53, 99],
    "Ops": lambda x: (x + 8),
    "Test": lambda x: (x % 13) == 0,
    "Target": (1, 2),
}
M[4] = {
    "items": [52, 62, 94, 96, 52, 87, 53, 60],
    "Ops": lambda x: (x * x),
    "Test": lambda x: (x % 19) == 0,
    "Target": (3, 1),
}

M[5] = {
    "items": [94, 80, 84, 79],
    "Ops": lambda x: (x + 5),
    "Test": lambda x: (x % 2) == 0,
    "Target": (7, 0),
}
M[6] = {
    "items": [89],
    "Ops": lambda x: (x + 1),
    "Test": lambda x: (x % 3) == 0,
    "Target": (0, 5),
}

M[7] = {
    "items": [70, 59, 63],
    "Ops": lambda x: (x + 3),
    "Test": lambda x: (x % 7) == 0,
    "Target": (4, 3),
}
I = Counter()
# this is the Chinese Remainder Theorem. Each time after operation, we can reduce the
# number by mod-ing it by the product of all test.
N = 7 * 3 * 2 * 19 * 13 * 5 * 17 * 11
for r in range(10000):
    for m in range(len(M)):
        I[m] += len(M[m]["items"])
        while M[m]["items"]:
            item = M[m]["items"].pop()
            w = M[m]["Ops"](item) % N
            if M[m]["Test"](w):
                M[M[m]["Target"][0]]["items"].append(w)
            else:
                M[M[m]["Target"][1]]["items"].append(w)

print(f"Part 2: {prod(k[1] for k in I.most_common(2))}")
