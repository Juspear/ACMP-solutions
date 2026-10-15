with open('input.txt') as f:
    data = list(map(int, f.read().split()))

positions = data[1:data[0] + 1]

limit = 200000
sieve = bytearray([1]) * limit
sieve[0] = sieve[1] = 0
for i in range(2, int(limit ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(range(i * i, limit, i)))

row = ''.join(str(i) for i in range(limit) if sieve[i])

with open('output.txt', 'w') as f:
    f.write(''.join(row[p - 1] for p in positions) + '\n')
