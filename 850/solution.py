a, b = map(int, open("input.txt").read().split())
low = (max(a, b) + 1) // 2
high = min(a, b)
open("output.txt", "w").write(f"{low} {high}")
