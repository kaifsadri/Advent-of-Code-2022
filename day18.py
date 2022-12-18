D = dict(
    (p, 6)
    for p in set(
        tuple(map(lambda x: int(x), line.strip().split(",")))
        for line in open("day18.txt").readlines()
    )
)
A = {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}


# part 1: just count the exposed surfaces by removing adjacent ones
for p in D:
    for a in A:
        if (p[0] + a[0], p[1] + a[1], p[2] + a[2]) in D:
            D[p] -= 1
print(f"Part 1: {sum(D.values())}")

# Part 2: BFS starting from a point confirmed to be outside the droplet
mn_x, mx_x = min(p[0] for p in D) - 2, max(p[0] for p in D) + 2
mn_y, mx_y = min(p[1] for p in D) - 2, max(p[1] for p in D) + 2
mn_z, mx_z = min(p[2] for p in D) - 2, max(p[2] for p in D) + 2
# start at a point confirmed to be outside the droplet, not touching nothing
ToGo = {(mn_x, mn_y, mn_z)}
Been = set()
S = dict()
while ToGo:
    p = ToGo.pop()
    Been.add(p)
    for a in A:
        x = (p[0] + a[0], p[1] + a[1], p[2] + a[2])
        if mn_x <= x[0] <= mx_x and mn_y <= x[1] <= mx_y and mn_z <= x[2] <= mx_z:
            if x in D:
                S[p] = S.get(p, 0) + 1
            elif x not in Been:
                ToGo.add(x)
            else:
                pass
print(f"Part 2: {sum(S.values())}")
