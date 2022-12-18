D = dict()
S = E = (0, 0)
O = dict()  # set of all "a"
for r, row in enumerate(open("day12.txt").readlines()):
    for c, char in enumerate(row.strip()):
        if char == "a":
            D[(r, c)] = ord(char)
            O[(r, c)] = 0
        elif char == "S":
            S = (r, c)
            D[S] = ord("a")
            O[(r, c)] = 0
        elif char == "E":
            E = (r, c)
            D[E] = ord("z")
        else:
            D[(r, c)] = ord(char)
A = {(1, 0), (-1, 0), (0, 1), (0, -1)}
N = 1_000_000  # some large number to use below

# Part 1: BFS with tracking the num of steps it takes to get to each
ToGo = {S: 0}
Been = dict()
while ToGo:
    p = ToGo.popitem()
    Been[p[0]] = p[1]
    for a in A:
        x = (p[0][0] + a[0], p[0][1] + a[1])
        if (
            ToGo.get(x, N) > p[1] + 1
            and D.get(x, N) - D[p[0]] <= 1
            and Been.get(x, N) > Been[p[0]] + 1
        ):
            ToGo[x] = p[1] + 1
print(f"Part 1: {Been[E]}")

# Part 2: Do the same thing for every "a" square
# trick: start from any random "a" point, but as soon as
# the path hits another "a", abort and follow that "a"
# this re-uses Been from P1
Been.update(O)
while O:
    o = O.popitem()
    ToGo = {o[0]: o[1]}
    while ToGo:
        p = ToGo.popitem()
        if p[0] in O:
            break
        Been[p[0]] = p[1]
        for a in A:
            x = (p[0][0] + a[0], p[0][1] + a[1])
            if (
                ToGo.get(x, N) > p[1] + 1
                and D.get(x, N) - D[p[0]] <= 1
                and Been.get(x, N) > Been[p[0]] + 1
            ):
                ToGo[x] = p[1] + 1
print(f"Part 2: {Been[E]}")
