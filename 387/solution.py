with open("input.txt") as f:
    lines = f.read().split("\n")

n = int(lines[0])
count = 0
for rule in lines[1:n + 1]:
    rule = rule.strip()
    left = rule[0]
    right = rule[rule.index(">") + 1:].strip()
    if right and right[0] == left:
        count += 1

with open("output.txt", "w") as f:
    f.write(str(count))
