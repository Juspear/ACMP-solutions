k, n = map(int, open("input.txt").read().split())
page = (n - 1) // k + 1
line = (n - 1) % k + 1
open("output.txt", "w").write(f"{page} {line}")
