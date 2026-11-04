with open("input.txt") as f:
    n, v, k = map(int, f.read().split())

total = 0
empty = False
for day in range(n):
    portion = v - day * k
    if portion <= 0:
        empty = True
    else:
        total += portion

with open("output.txt", "w") as f:
    f.write(f"{'NO' if empty else 'YES'} {total}\n")
