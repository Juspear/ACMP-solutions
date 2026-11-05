m = int(open("input.txt").read())
with open("output.txt", "w") as f:
    f.write(str(int(bin(m)[2:][::-1], 2)))
