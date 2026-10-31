def digit_sum(n, p):
    s = 0
    while n:
        s += n % p
        n //= p
    return s


with open("input.txt") as f:
    n1, p1, n2, p2 = map(int, f.read().split())

a = digit_sum(n1, p1)
b = digit_sum(n2, p2)

with open("output.txt", "w") as f:
    f.write(f"{a if a == b else 0}\n")
