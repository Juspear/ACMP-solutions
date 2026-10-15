with open('input.txt') as f:
    n = int(f.read().strip())


def digit_sum(x):
    return sum(int(c) for c in str(x))


divisors = [d for d in range(1, n + 1) if n % d == 0]
best = min(divisors, key=lambda d: (-digit_sum(d), d))

with open('output.txt', 'w') as f:
    f.write(str(best) + '\n')
