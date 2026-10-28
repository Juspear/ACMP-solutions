import re

pattern = re.compile(r"[ABCEHKMOPTXY][0-9]{3}[ABCEHKMOPTXY]{2}")
lines = open("input.txt").read().split()
n = int(lines[0])
result = ["Yes" if pattern.fullmatch(s) else "No" for s in lines[1:n + 1]]
open("output.txt", "w").write("\n".join(result))
