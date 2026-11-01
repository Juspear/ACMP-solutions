with open("input.txt") as f:
    x = float(f.read().split()[0].replace(",", "."))

cards = 0
overhang = 0.0
while overhang < x - 1e-9:
    cards += 1
    overhang += 1 / (cards + 1)

with open("output.txt", "w") as f:
    f.write(f"{cards} card(s)")
