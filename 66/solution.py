keyboard = "qwertyuiopasdfghjklzxcvbnm"

with open("input.txt") as f:
    c = f.read().strip()

pos = keyboard.index(c)
answer = keyboard[(pos + 1) % len(keyboard)]

with open("output.txt", "w") as f:
    f.write(answer + "\n")
