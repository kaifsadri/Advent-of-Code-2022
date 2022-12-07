from functools import lru_cache

L = list(line.strip().split() for line in open("day07.txt").readlines())
FS = {"/": {"parent": "/", "dirs": set(), "files": set()}}
pwd = "/"

for line in L:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                pwd = FS[pwd]["parent"]
            elif line[2] != "/":
                nd = f"{pwd}{line[2]}/"
                try:
                    FS[nd]["parent"] = pwd
                except KeyError:
                    FS[nd] = {"parent": pwd}
                pwd = nd
            else:
                pwd = "/"
        elif line[1] == "ls":
            continue
    elif line[0] == "dir":
        FS[pwd]["dirs"] = FS[pwd].get("dirs", set()) | {f"{pwd}{line[1]}/"}
    else:  # some file here
        FS[pwd]["files"] = FS[pwd].get("files", set()) | {
            (int(line[0]), line[1])
        }


@lru_cache(maxsize=10_000)
def totalsize(d):
    global FS
    result = 0
    try:
        for f in FS[d]["files"]:
            result += f[0]
    except KeyError:
        pass
    try:
        for directory in FS[d]["dirs"]:
            result += totalsize(directory)
    except KeyError:
        pass
    return result


for directory in FS:
    FS[directory]["size"] = totalsize(directory)

P1 = 0
P2 = FS["/"]["size"]
needed = 30_000_000 - (70_000_000 - FS["/"]["size"])
for directory in FS:
    if FS[directory]["size"] <= 100_000:
        P1 += FS[directory]["size"]
    if FS[directory]["size"] >= needed and FS[directory]["size"] <= P2:
        P2 = FS[directory]["size"]
print(f"Part 1: {P1}")
print(f"Part 2: {P2}")
