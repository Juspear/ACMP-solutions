with open("input.txt") as f:
    s = int(f.read().split()[0])

goals = 0
while goals * (goals + 1) // 2 < s:
    goals += 1

with open("output.txt", "w") as f:
    f.write(str(goals))
