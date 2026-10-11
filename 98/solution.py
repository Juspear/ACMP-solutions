with open("input.txt") as f:
    data = list(map(int, f.read().split()))

a = data[1:data[0] + 1]
left, right = 0, len(a) - 1
score = [0, 0]
turn = 0

while left <= right:
    if a[left] >= a[right]:
        score[turn] += a[left]
        left += 1
    else:
        score[turn] += a[right]
        right -= 1
    turn ^= 1

with open("output.txt", "w") as f:
    f.write(f"{score[0]}:{score[1]}")
