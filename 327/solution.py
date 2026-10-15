def lucky(x):
    if x < 0 or x > 999999:
        return False
    s = f"{x:06d}"
    return sum(map(int, s[:3])) == sum(map(int, s[3:]))


with open("input.txt") as f:
    data = f.read().split()

k = int(data[0])
res = []
for t in data[1:k + 1]:
    x = int(t)
    res.append("Yes" if lucky(x - 1) or lucky(x + 1) else "No")

with open("output.txt", "w") as f:
    f.write("\n".join(res))
