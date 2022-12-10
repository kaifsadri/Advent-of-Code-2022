L = list(line.strip().split() for line in open("day10.txt").readlines())
x = 1
cycle = 0
C = dict()
for line in L:
    if "addx" == line[0]:
        cycle += 1
        C[cycle] = x
        cycle += 1
        C[cycle] = x
        x += int(line[1])
    elif "noop" == line[0]:
        cycle += 1
        C[cycle] = x

print(f"Part 1: {sum(c * C[c] for c in {20, 60, 100, 140, 180, 220})}")

print("Part 2:\n")
line = ""
for t in range(6 * 40):
    sprite = {C[t + 1] - 1, C[t + 1], C[t + 1] + 1}
    if t % 40 in sprite:
        line += "█"
    else:
        line += " "
    if (t + 1) % 40 == 0:
        print(line)
        line = ""
print()
