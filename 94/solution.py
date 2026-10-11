with open("input.txt") as f:
    n, m, k = map(int, f.read().split())

if m <= n:
    answer = "1"
elif n <= k:
    answer = "NO"
else:
    step = n - k
    answer = str(1 + (m - n + step - 1) // step)

with open("output.txt", "w") as f:
    f.write(answer)
