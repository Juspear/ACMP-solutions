lines = open('input.txt').read().split()
n, m = int(lines[0]), int(lines[1])
best = m
for row in lines[2:2 + n]:
    last_a = row.rfind('A')
    first_b = row.find('B')
    best = min(best, first_b - last_a - 1)
open('output.txt', 'w').write(str(best))
