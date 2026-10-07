with open("input.txt") as f:
    s = f.read().strip()

digits = [int(c) for c in s]
lucky = sum(digits[:3]) == sum(digits[3:])

with open("output.txt", "w") as f:
    f.write("YES\n" if lucky else "NO\n")
