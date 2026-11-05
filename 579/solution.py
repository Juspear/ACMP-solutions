data = list(map(int, open("input.txt").read().split()))
n = data[0]
a = data[1:1 + n]
pos = [i + 1 for i in range(n) if a[i] > 0]
neg = [i + 1 for i in range(n) if a[i] < 0]
pos_sum = sum(a[i - 1] for i in pos)
neg_sum = -sum(a[i - 1] for i in neg)
best = pos if pos_sum >= neg_sum else neg
if not best:
    best = [1]
with open("output.txt", "w") as f:
    f.write(str(len(best)) + "\n" + " ".join(map(str, best)))
