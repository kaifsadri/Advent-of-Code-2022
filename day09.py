L = list(line.strip().split() for line in open("day09.txt").readlines())

Moves = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
HV = {(0, 1), (0, -1), (-1, 0), (1, 0)}
TV = {(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)}
H = (0, 0)
T = (0, 0)

TP = {T}
for line in L:
    for m in range(int(line[1])):
        H = (H[0] + Moves[line[0]][0], H[1] + Moves[line[0]][1])
        d = (abs(H[0] - T[0]), abs(H[1] - T[1]))
        if abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1:
            target = set((H[0] + x[0], H[1] + x[1]) for x in HV) & set(
                (T[0] + x[0], T[1] + x[1]) for x in TV
            )
            T = target.pop()
            TP.add(T)
print(f"Part 1: {len(TP)}")

K = [(0, 0)] * 10  # K[0] is the head. Rest are tail knots.
TP = {(0, 0)}
for line in L:
    for m in range(int(line[1])):
        K[0] = (K[0][0] + Moves[line[0]][0], K[0][1] + Moves[line[0]][1])
        for n in range(1, 10):
            d = (abs(K[n - 1][0] - K[n][0]), abs(K[n - 1][1] - K[n][1]))
            if d in {
                (2, 2),
                (0, 2),
                (2, 0),
            }:  # tail knot needs to jump diagonally to catch up
                K[n] = ((K[n - 1][0] + K[n][0]) // 2, (K[n - 1][1] + K[n][1]) // 2)
            elif d in {(2, 1), (1, 2)}:  # move like in part 1
                target = set((K[n - 1][0] + x[0], K[n - 1][1] + x[1]) for x in HV) & set(
                    (K[n][0] + x[0], K[n][1] + x[1]) for x in TV
                )
                K[n] = target.pop()
            else:  # if this knot is not moving, none of the ones after it are:
                break
        TP.add(K[9])  # this is repetitive, but not expensive
print(f"Part 2: {len(TP)}")
