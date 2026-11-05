with open("input.txt") as f:
    word = f.read().strip()

ok = word[0].isupper()
length = 0
for ch in word:
    if ch.isupper():
        if length and not 2 <= length <= 4:
            ok = False
            break
        length = 1
    else:
        length += 1
if not 2 <= length <= 4:
    ok = False

with open("output.txt", "w") as f:
    f.write("Yes\n" if ok else "No\n")
