with open("input.txt") as f:
    num, marks = f.read().split()

n = int(num)
k = len(marks)

result = 1
while n > 0:
    result *= n
    n -= k

with open("output.txt", "w") as f:
    f.write(str(result))
