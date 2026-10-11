with open("input.txt") as f:
    n = int(f.read())

fives = n // 5
while (n - 5 * fives) % 3 != 0:
    fives -= 1

with open("output.txt", "w") as f:
    f.write(f"{fives} {(n - 5 * fives) // 3}")
