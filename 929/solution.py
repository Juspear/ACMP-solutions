n = int(open("input.txt").read())
dice = (n + 5) // 6
open("output.txt", "w").write(f"{7 * dice - n} {6 * n}")
