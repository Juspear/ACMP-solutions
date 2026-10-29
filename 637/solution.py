data = list(map(int, open('input.txt').read().split()))
n = data[0]
a = data[1:n + 1]
k = data[n + 1]
open('output.txt', 'w').write(str(sum(min(x, k) for x in a)))
