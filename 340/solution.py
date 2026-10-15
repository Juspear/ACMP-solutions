with open("input.txt") as f:
    data = list(map(int, f.read().split()))

a = sorted(data[:3])
b = sorted(data[3:6])

if a == b:
    ans = "Boxes are equal"
elif all(x <= y for x, y in zip(a, b)):
    ans = "The first box is smaller than the second one"
elif all(x >= y for x, y in zip(a, b)):
    ans = "The first box is larger than the second one"
else:
    ans = "Boxes are incomparable"

with open("output.txt", "w") as f:
    f.write(ans)
