with open("input.txt") as f:
    digits = sorted(f.read().strip())

largest = "".join(reversed(digits))
first = next(i for i, d in enumerate(digits) if d != "0")
smallest = digits[first] + "".join(digits[:first] + digits[first + 1:])

with open("output.txt", "w") as f:
    f.write(f"{smallest} {largest}\n")
