x1, y1, x2, y2 = map(int, open("input.txt").read().split())
length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
text = f"{length:.6f}".rstrip("0").rstrip(".")
open("output.txt", "w").write(text)
