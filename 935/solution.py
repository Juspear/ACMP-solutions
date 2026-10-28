x1, y1, x2, y2 = map(int, open("input.txt").read().split())
same = (x1 + y1) % 2 == (x2 + y2) % 2
open("output.txt", "w").write("YES" if same else "NO")
