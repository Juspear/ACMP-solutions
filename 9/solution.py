with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:n + 1]

positive = sum(x for x in a if x > 0)
i, j = a.index(min(a)), a.index(max(a))
if i > j:
    i, j = j, i

product = 1
for x in a[i + 1:j]:
    product *= x

with open('output.txt', 'w') as f:
    f.write(f'{positive} {product}\n')
