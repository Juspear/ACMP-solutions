p, k = map(int, open("input.txt").read().split())
total = 0
for x in range(p, k + 1):
    while x != 2:
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        total += 1
with open("output.txt", "w") as f:
    f.write(str(total))
