with open("input.txt") as f:
    n, m = map(int, f.read().split())

cnt = [0] * 30
for j in range(1, m + 1):
    cnt[j % 30] += 1

red = green = blue = black = 0
for i in range(1, n + 1):
    for r in range(30):
        if not cnt[r]:
            continue
        v = i * r % 30
        if v % 5 == 0:
            blue += cnt[r]
        elif v % 3 == 0:
            green += cnt[r]
        elif v % 2 == 0:
            red += cnt[r]
        else:
            black += cnt[r]

with open("output.txt", "w") as f:
    f.write(f"RED : {red}\nGREEN : {green}\nBLUE : {blue}\nBLACK : {black}\n")
