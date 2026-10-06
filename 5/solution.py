with open('input.txt') as f:
    data = f.read().split()

n = int(data[0])
days = data[1:n + 1]

odd = [d for d in days if int(d) % 2 == 1]
even = [d for d in days if int(d) % 2 == 0]

with open('output.txt', 'w') as f:
    f.write(' '.join(odd) + '\n')
    f.write(' '.join(even) + '\n')
    f.write('YES' if len(even) >= len(odd) else 'NO')
