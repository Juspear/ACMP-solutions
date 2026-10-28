data = open("input.txt").read().split()
k = int(data[0])
s = data[1]
open("output.txt", "w").write(s[:k - 1] + s[k:])
