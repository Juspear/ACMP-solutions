l, w, h = map(int, open("input.txt").read().split())
area = 2 * (l + w) * h
open("output.txt", "w").write(str((area + 15) // 16))
