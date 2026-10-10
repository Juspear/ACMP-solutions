s, t = map(int, open("input.txt").read().split())
open("output.txt", "w").write(str((t - s) % 12))
