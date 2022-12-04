L = list(line.strip() for line in open("day04.txt", "r").readlines())

P1 = 0
P2 = 0
for line in L:
    elf1, elf2 = line.split(",")
    elf1 = tuple(map(int, elf1.split("-")))
    elf2 = tuple(map(int, elf2.split("-")))
    # check if either elf is fully covered by the other
    if (elf1[0] <= elf2[0] <= elf1[1] and elf1[0] <= elf2[1] <= elf1[1]) or (
        elf2[0] <= elf1[0] <= elf2[1] and elf2[0] <= elf1[1] <= elf2[1]
    ):
        P1 += 1
    if (elf1[0] <= elf2[0] <= elf1[1] or elf1[0] <= elf2[1] <= elf1[1]) or (
        elf2[0] <= elf1[0] <= elf2[1] or elf2[0] <= elf1[1] <= elf2[1]
    ):
        P2 += 1

print(f"Part 1: {P1}")
print(f"Part 2: {P2}")
