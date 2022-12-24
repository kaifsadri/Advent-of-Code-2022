P = set(line.strip().replace(":", " =") for line in open("day21.txt").readlines())

# For part one, we just evaluate equations until root speaks
L = P.copy()
while True:
    try:
        print(f"Part 1: {int(root)}")
        break
    except NameError:
        pass
    try:
        exp = L.pop()
        exec(exp)
    except NameError:
        L.add(exp)

# For part two, we re-organize the equations until humn checks out

# clear all locals first
for item in locals().copy():
    if item != "P":
        del globals()[item]

L = P.copy()
for exp in P:
    if exp.startswith("humn"):
        L.remove(exp)  # get rid of humn
        continue
    elif exp.startswith("root"):  # re-arrange root for equality
        L.remove(exp)
        L.add(f"{exp[7:11]} = {exp[14:]}")
        L.add(f"{exp[14:]} = {exp[7:11]}")
        continue
    else:
        try:  # format is a = b op c
            a, b, op, c = exp[:4], exp[7:11], exp[12], exp[14:]
        except IndexError:
            continue  # this leaves lines like hgas = 67 alone
        if op == "+":
            L.add(f"{b} = {a} - {c}")
            L.add(f"{c} = {a} - {b}")
        elif op == "/":
            L.add(f"{b} = {a} * {c}")
            L.add(f"{c} = {b} / {a}")
        elif op == "-":
            L.add(f"{b} = {c} + {a}")
            L.add(f"{c} = {b} - {a}")
        elif op == "*":
            L.add(f"{b} = {a} / {c}")
            L.add(f"{c} = {a} / {b}")

# now solve for humn like it was done for root in part 1
while True:
    try:
        print(f"Part 2: {int(humn)}")
        break
    except NameError:
        pass
    try:
        exp = L.pop()
        exec(exp)
    except NameError:
        L.add(exp)
