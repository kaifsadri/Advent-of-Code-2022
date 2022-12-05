"""
        [Q] [B]         [H]        
    [F] [W] [D] [Q]     [S]        
    [D] [C] [N] [S] [G] [F]        
    [R] [D] [L] [C] [N] [Q]     [R]
[V] [W] [L] [M] [P] [S] [M]     [M]
[J] [B] [F] [P] [B] [B] [P] [F] [F]
[B] [V] [G] [J] [N] [D] [B] [L] [V]
[D] [P] [R] [W] [H] [R] [Z] [W] [S]
 1   2   3   4   5   6   7   8   9 
"""
from collections import deque

S = {
    1: deque("VJBD"),
    2: deque("FDRWBVP"),
    3: deque("QWCDLFGR"),
    4: deque("BDNLMPJW"),
    5: deque("QSCPBNH"),
    6: deque("GNSBDR"),
    7: deque("HSFQMPBZ"),
    8: deque("FLW"),
    9: deque("RMFVS"),
}
L = list(line.strip() for line in open("day05.txt", "r").readlines()[10:])
for line in L:
    l = line.split()
    n, f, t = int(l[1]), int(l[3]), int(l[5])
    for _ in range(n):
        S[t].appendleft(S[f].popleft())
print("Part 1: ", end="")
for k in range(1, 10):
    print(S[k].popleft(), end="")
print()

S = {
    1: deque("VJBD"),
    2: deque("FDRWBVP"),
    3: deque("QWCDLFGR"),
    4: deque("BDNLMPJW"),
    5: deque("QSCPBNH"),
    6: deque("GNSBDR"),
    7: deque("HSFQMPBZ"),
    8: deque("FLW"),
    9: deque("RMFVS"),
}

for line in L:
    l = line.split()
    n, f, t = int(l[1]), int(l[3]), int(l[5])
    s = list()
    for _ in range(n):
        s.append(S[f].popleft())
    for _ in range(n):
        S[t].appendleft(s.pop())

print("Part 2: ", end="")
for k in range(1, 10):
    print(S[k].popleft(), end="")
print()
