with open("input.txt") as f:
    k = int(f.read())

count = 0
for x in range(1, k + 1):
    if x + int(str(x)[::-1]) == k:
        count += 1

with open("output.txt", "w") as f:
    f.write(str(count) + "\n")
