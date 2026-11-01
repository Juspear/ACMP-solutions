with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
answers = data[1:1 + n]

cost = 3
score = 0
for a in answers:
    if a == "1":
        score += cost
        cost += 1
    else:
        cost = max(3, cost - 3)

with open("output.txt", "w") as f:
    f.write(str(score))
