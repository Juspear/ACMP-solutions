with open("input.txt") as f:
    s = f.read().strip()

col = ord(s[0].upper()) - ord("A")
row = int(s[1]) - 1
color = "BLACK" if (col + row) % 2 == 0 else "WHITE"

with open("output.txt", "w") as f:
    f.write(color + "\n")
