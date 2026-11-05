lines = open("input.txt").read().split("\n")
rooms = int(lines[0])
pos = 1
people = []
for _ in range(rooms):
    cnt = int(lines[pos])
    pos += 1
    for _ in range(cnt):
        score, name = lines[pos].split()
        pos += 1
        cents = round(float(score) * 100)
        people.append((cents, name))
people.sort(key=lambda x: -x[0])
out = [str(len(people))]
for cents, name in people:
    sign = "-" if cents < 0 else ""
    c = abs(cents)
    out.append(f"{sign}{c // 100}.{c % 100:02d} {name}")
with open("output.txt", "w") as f:
    f.write("\n".join(out))
