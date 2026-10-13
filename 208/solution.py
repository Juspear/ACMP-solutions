with open('input.txt') as f:
    n = int(f.read().strip())

bits = bin(n)[2:]
best = max(int(bits[i:] + bits[:i], 2) for i in range(len(bits)))

with open('output.txt', 'w') as f:
    f.write(str(best) + '\n')
