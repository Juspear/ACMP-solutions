with open("input.txt") as f:
    data = list(map(int, f.read().split()))

k, w = data[0], data[1]
tents = [(data[2], data[3]), (data[4], data[5]), (data[6], data[7])]

possible = False
for mask in range(1, 8):
    weight = sum(tents[i][0] for i in range(3) if mask >> i & 1)
    places = sum(tents[i][1] for i in range(3) if mask >> i & 1)
    if weight <= w and places >= k:
        possible = True

with open("output.txt", "w") as f:
    f.write("YES" if possible else "NO")
