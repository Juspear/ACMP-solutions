with open("input.txt") as f:
    k = int(f.read())

wait = 5 * (k - 1)

with open("output.txt", "w") as f:
    if wait > 720:
        f.write("NO")
    else:
        f.write(f"{wait // 60} {wait % 60}")
