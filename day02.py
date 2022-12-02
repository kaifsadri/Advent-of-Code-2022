L = list(line.strip().split() for line in open("day02.txt", "r").readlines())


def Play(player, me):
    Move = {
        "X": {"equals": "A", "score": 1, "wins": "C"},
        "Y": {"equals": "B", "score": 2, "wins": "A"},
        "Z": {"equals": "C", "score": 3, "wins": "B"},
    }
    if Move[me]["wins"] == player:
        return Move[me]["score"] + 6
    elif Move[me]["equals"] == player:
        return Move[me]["score"] + 3
    else:
        return Move[me]["score"]


print(f"Part 1: {sum(Play(line[0],line[1]) for line in L)}")

Score = {
    "A": {"X": 3 + 0, "Y": 1 + 3, "Z": 2 + 6},
    "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
    "C": {"X": 2 + 0, "Y": 3 + 3, "Z": 1 + 6},
}
print(f"Part 2: {sum(Score[line[0]][line[1]] for line in L)}")
