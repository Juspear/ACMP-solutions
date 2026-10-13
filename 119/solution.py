with open('input.txt') as f:
    data = f.read().split()

n = int(data[0])
times = []
for i in range(n):
    h, m, s = map(int, data[1 + 3 * i:4 + 3 * i])
    times.append((h, m, s))

times.sort()

with open('output.txt', 'w') as f:
    f.write('\n'.join(f'{h} {m} {s}' for h, m, s in times) + '\n')
