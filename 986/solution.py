with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, bx, by, length = data[:4]
answer = "Yes"
for i in range(n):
    x, y = data[4 + 2 * i], data[5 + 2 * i]
    if (x - bx) ** 2 + (y - by) ** 2 <= length * length:
        answer = str(i + 1)
        break

with open("output.txt", "w") as f:
    f.write(answer + "\n")
