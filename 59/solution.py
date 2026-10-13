with open('input.txt') as f:
    n, k = map(int, f.read().split())

digits = []
while n > 0:
    digits.append(n % k)
    n //= k

product = 1
for d in digits:
    product *= d

with open('output.txt', 'w') as f:
    f.write(str(product - sum(digits)) + '\n')
