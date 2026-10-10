data = open("input.txt").read().split()
room, target, mode = int(data[0]), int(data[1]), data[2]
if mode == "freeze":
    result = min(room, target)
elif mode == "heat":
    result = max(room, target)
elif mode == "auto":
    result = target
else:
    result = room
open("output.txt", "w").write(str(result))
