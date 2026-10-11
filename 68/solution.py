with open("input.txt") as f:
    place = f.readline().strip()
    x = int(f.readline())

if place == "Home" or x % 2 == 1:
    answer = "Yes"
else:
    answer = "No"

with open("output.txt", "w") as f:
    f.write(answer)
