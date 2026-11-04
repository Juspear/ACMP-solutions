with open("input.txt") as f:
    mode, n, a, b, c = map(int, f.read().split())

if mode == 2:
    answer = min(a, b, c)
else:
    answer = max(0, a + b + c - 2 * n)

with open("output.txt", "w") as f:
    f.write(f"{answer}\n")
