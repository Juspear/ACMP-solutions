with open("input.txt") as f:
    s = f.read().strip()

result = []
count = ""
for ch in s:
    if ch.isdigit():
        count += ch
    else:
        result.append(ch * (int(count) if count else 1))
        count = ""

text = "".join(result)
lines = [text[i:i + 40] for i in range(0, len(text), 40)]

with open("output.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
