with open("input.txt") as f:
    s = f.read().strip()

zeros = len(s) - len(s.rstrip("0"))

with open("output.txt", "w") as f:
    f.write("1" + "0" * zeros)
