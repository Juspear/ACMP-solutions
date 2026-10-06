with open('input.txt') as f:
    n = int(f.read())

if n >= 1:
    s = n * (n + 1) // 2
else:
    s = (1 + n) * (2 - n) // 2

with open('output.txt', 'w') as f:
    f.write(str(s))
