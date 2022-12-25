# here we just add these SNAFU numbers directly in SNAFU base
nums = list(list(line.strip()) for line in open("day25.txt").readlines())
answer = list()  # This will the reversed version of the final answer
c = 0
while True:
    done = True
    for number in nums:
        try:
            match (d := number.pop()):
                case "0" | "1" | "2":
                    c += int(d)
                case "-":
                    c -= 1
                case "=":
                    c -= 2
            done = False
        except IndexError:
            pass
    if done:
        break
    c, r = divmod(c, 5)
    match r:
        case 0 | 1 | 2:
            answer.append(str(r))
        case 3:
            c += 1
            answer.append("=")
        case 4:
            c += 1
            answer.append("-")
print(f" Part 1: {''.join(answer[-1::-1])}")
