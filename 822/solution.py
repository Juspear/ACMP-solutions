x1, y1, x2, y2, x3, y3 = map(int, open("input.txt").read().split())
doubled = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
if doubled % 2 == 0:
    answer = str(doubled // 2)
else:
    answer = f"{doubled // 2}.5"
open("output.txt", "w").write(answer)
