with open('input.txt') as f:
    n = int(f.read())

total = 0
for d in range(1, n + 1):
    if n % d == 0:
        total += d

with open('output.txt', 'w') as f:
    f.write(str(total))
