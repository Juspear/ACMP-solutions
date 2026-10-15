with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
costs = data[1:n + 1]
bonus = data[n + 1]
m = data[n + 2]
pos = n + 3

best = 0
results = []
for attempt in range(m):
    passed = data[pos:pos + n]
    pos += n
    score = sum(c for c, p in zip(costs, passed) if p)
    if all(passed):
        score += bonus
    best = max(best, score - 2 * attempt)
    results.append(best)

with open('output.txt', 'w') as f:
    f.write('\n'.join(map(str, results)) + '\n')
