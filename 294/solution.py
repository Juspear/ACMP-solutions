with open("input.txt") as f:
    k1, l1, m1, k2, l2, m2 = map(int, f.read().split())

bolts = k1 * (100 - l1) // 100
nuts = k2 * (100 - l2) // 100
pairs = min(bolts, nuts)

damage = (k1 - pairs) * m1 + (k2 - pairs) * m2

with open("output.txt", "w") as f:
    f.write(f"{damage}\n")
