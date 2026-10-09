with open("input.txt") as f:
    s, p = map(int, f.read().split())

answer = None
for x in range(1, s // 2 + 1):
    y = s - x
    if x * y == p:
        answer = (x, y)
        break

with open("output.txt", "w") as f:
    f.write(f"{answer[0]} {answer[1]}\n")
