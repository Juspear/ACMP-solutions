with open("input.txt") as f:
    h1, m1, h2, m2 = map(int, f.read().split())

start = h1 * 60 + m1
end = h2 * 60 + m2
if end < start:
    end += 24 * 60

strikes = 0
for t in range(start + 1, end + 1):
    minute = t % (24 * 60)
    if minute % 60 == 30:
        strikes += 1
    elif minute % 60 == 0:
        hour = minute // 60 % 12
        strikes += hour if hour else 12

with open("output.txt", "w") as f:
    f.write(str(strikes) + "\n")
