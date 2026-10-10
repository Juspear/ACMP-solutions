a, b, c = sorted(map(int, open("input.txt").read().split()))
open("output.txt", "w").write("YES" if a + b > c else "NO")
