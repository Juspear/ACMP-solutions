with open("input.txt") as f:
    n = int(f.read())

result = n
x = n
p = 2
while p * p <= x:
    if x % p == 0:
        while x % p == 0:
            x //= p
        result -= result // p
    p += 1
if x > 1:
    result -= result // x
if n == 1:
    result = 0

with open("output.txt", "w") as f:
    f.write(str(result))
