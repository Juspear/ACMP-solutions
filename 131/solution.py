with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
best_age = -1
best_index = -1
for i in range(n):
    age = data[1 + 2 * i]
    sex = data[2 + 2 * i]
    if sex == 1 and age > best_age:
        best_age = age
        best_index = i + 1

with open("output.txt", "w") as f:
    f.write(str(best_index) + "\n")
