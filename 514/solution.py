with open("input.txt") as f:
    k = int(f.read())

h = 0
while k >= h + 1:
    h += 1
    k -= h

with open("output.txt", "w") as f:
    f.write(str(h))
