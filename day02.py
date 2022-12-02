L = open("day02.txt", "r").readlines()

Game = {
    "A X\n": 4,
    "A Y\n": 8,
    "A Z\n": 3,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 7,
    "C Y\n": 2,
    "C Z\n": 6,
}
print(f"Part 1: {sum(Game[line] for line in L)}")

Game = {
    "A X\n": 3,
    "A Y\n": 4,
    "A Z\n": 8,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 2,
    "C Y\n": 6,
    "C Z\n": 7,
}
print(f"Part 2: {sum(Game[line] for line in L)}")
