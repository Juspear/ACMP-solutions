with open("input.txt") as f:
    g = [line.strip() for line in f if line.strip()]

ok = True
for i in range(3):
    for j in range(3):
        if g[i][j] == g[i][j + 1] == g[i + 1][j] == g[i + 1][j + 1]:
            ok = False

with open("output.txt", "w") as f:
    f.write("Yes\n" if ok else "No\n")
