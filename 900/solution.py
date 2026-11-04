with open("input.txt") as f:
    n = int(f.read())

x = n // 3
petya = 13 * x // 8
vasya = x // 2
kolya = 7 * x // 8

with open("output.txt", "w") as f:
    f.write(f"{petya} {vasya} {kolya}\n")
