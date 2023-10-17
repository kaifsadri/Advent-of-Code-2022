# Part 1
S = dict()  # sensors and their closest beacon
B = set()  # Beacons
for line in open("day15.txt").read().strip().split("\n"):
    sx = int(line[line.find("x=") + 2 : line.find(",")])
    sy = int(line[line.find("y=") + 2 : line.find(":")])
    bx = int(line[line.rfind("x=") + 2 : line.rfind(",")])
    by = int(line[line.rfind("y=") + 2 :])
    S[(sx, sy)] = (bx, by)
    B.add((bx, by))

N = set()  # collect all the points that cannot be beacons
param = 2_000_000  # limit the search to line 2e6
for p in S:
    d = abs(S[p][0] - p[0]) + abs(S[p][1] - p[1])
    for x in range(p[0] - d, p[0] + d + 1):
        if (abs(x - p[0]) + abs(param - p[1])) <= d and (x, param) not in B:
            N.add((x, param))
print(f"Part 1: {len(N)}")


# part 2
# Now we are looking for a beacon just outside a sensor's detection,
# but also outside the detection areas of all other sensors.

R = dict()  # radii of each sensor
for s in S:
    R[s] = abs(s[0] - S[s][0]) + abs(s[1] - S[s][1])


def skin(sensor, M):
    """Returns the outer edge of the area detected by the sensor
    limited to coordinates 0..M"""
    global S, R
    x, y = sensor
    radius = R[sensor] + 1
    tx, ty = x, y + radius
    bx, by = x, y - radius
    rx, ry = x + radius, y
    lx, ly = x - radius, y
    res = set()
    while lx != rx:
        if 0 <= tx <= M and 0 <= ty <= M:
            res.add((tx, ty))
        if 0 <= rx <= M and 0 <= ry <= M:
            res.add((rx, ry))
        if 0 <= lx <= M and 0 <= ly <= M:
            res.add((lx, ly))
        if 0 <= bx <= M and 0 <= by <= M:
            res.add((bx, by))
        tx += 1
        ty -= 1
        rx -= 1
        ry -= 1
        bx -= 1
        by += 1
        lx += 1
        ly += 1
    return res


param = 4_000_000
for sensor in R:
    sk = skin(sensor, param)
    for candidate in sk:
        v = True  # if it is a viable candidate
        for s in R:
            if (abs(s[0] - candidate[0]) + abs(s[1] - candidate[1])) <= R[s]:
                v = False
                break  # move on to the next candidate
        if v:
            # if it is the right candidate, end the search
            print(f"Part 2: {candidate[0]*param+candidate[1]}")
            break
    if v:
        # end search here
        break
