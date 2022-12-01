L = list(line.strip() for line in open("day01.txt", "r").readlines())

Top3 = [0, 0, 0]  # There may be a duplicate in the Top 3, so cannot use sets
Elf = 0

while L:
    match L.pop():
        case "":
            if Elf > (m := min(Top3)):
                # swap this elf with the first lowest calorie elf
                Top3.remove(m)
                Top3.append(Elf)
            Elf = 0
        case calorie:
            Elf += int(calorie)
calorie
print(f"Part 1: {max(Top3)}")
print(f"Part 2: {sum(Top3)}")
