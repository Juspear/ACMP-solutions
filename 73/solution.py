digits = "0123456789ABCDEFGHIJKLMNOPQ"

with open("input.txt") as f:
    s = f.read().strip()

result = []
for pos, ch in enumerate(s, 1):
    code = (digits.index(ch) - pos) % 27
    if code == 0:
        result.append(" ")
    else:
        result.append(chr(ord("a") + code - 1))

with open("output.txt", "w") as f:
    f.write("".join(result) + "\n")
