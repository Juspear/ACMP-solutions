with open("input.txt") as f:
    h, m = map(int, f.read().strip().split(":"))

minutes = h * 60 + m
while True:
    minutes = (minutes + 1) % 1440
    time = f"{minutes // 60:02d}:{minutes % 60:02d}"
    if time == time[::-1]:
        break

with open("output.txt", "w") as f:
    f.write(time + "\n")
