s = open("input.txt").read().strip()
open("output.txt", "w").write("NO" if "0" in s else "YES")
