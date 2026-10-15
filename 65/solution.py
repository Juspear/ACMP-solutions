with open('input.txt') as f:
    lines = f.read().split()

s = lines[0]
n = int(lines[1])
messages = lines[2:2 + n]

dist = [sum(a != b for a, b in zip(s, m)) for m in messages]
best = min(dist)
indices = [i + 1 for i, d in enumerate(dist) if d == best]

with open('output.txt', 'w') as f:
    f.write(str(len(indices)) + '\n' + ' '.join(map(str, indices)) + '\n')
