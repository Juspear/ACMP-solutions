n = int(open("input.txt").read())
row, col = divmod(n - 1, 8)
result = []
for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    r, c = row + dr, col + dc
    if 0 <= r < 8 and 0 <= c < 8:
        result.append(r * 8 + c + 1)
open("output.txt", "w").write(" ".join(map(str, sorted(result))))
