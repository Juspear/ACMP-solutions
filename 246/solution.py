with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
cars = data[1:n + 1]

cuts = sum(1 for i in range(n - 1) if cars[i + 1] != cars[i] + 1)

with open('output.txt', 'w') as f:
    f.write(str(cuts) + '\n')
