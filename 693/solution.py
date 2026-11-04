with open("input.txt") as f:
    first, second = f.read().split()

same = sorted(first.lower()) == sorted(second.lower())

with open("output.txt", "w") as f:
    f.write("Yes\n" if same else "No\n")
