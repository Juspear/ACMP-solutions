with open('input.txt') as f:
    n = int(f.read().strip())

line = ''.join(str(i) for i in range(1, n + 1))
pos = line.find(str(n)) + 1

with open('output.txt', 'w') as f:
    f.write(str(pos) + '\n')
