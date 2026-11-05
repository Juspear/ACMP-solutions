with open("input.txt") as f:
    data = f.read().split()

k = int(data[0])
answers = []
for i in range(k):
    a, b = data[1 + 2 * i], data[2 + 2 * i]
    answers.append("YES" if set(a) == set(b) else "NO")

with open("output.txt", "w") as f:
    f.write("\n".join(answers) + "\n")
