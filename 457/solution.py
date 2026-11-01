with open("input.txt") as f:
    n = int(f.read().split()[0])

steps = 0
while True:
    digits = sorted(f"{n:04d}")
    big = int("".join(reversed(digits)))
    small = int("".join(digits))
    nxt = big - small
    if nxt == n:
        break
    n = nxt
    steps += 1

with open("output.txt", "w") as f:
    f.write(f"{n}\n{steps}\n")
