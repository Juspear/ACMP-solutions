k = int(open("input.txt").read())
flowers = ["G", "C", "V"]
for _ in range(k):
    flowers[1], flowers[2] = flowers[2], flowers[1]
    flowers[0], flowers[1] = flowers[1], flowers[0]
open("output.txt", "w").write("".join(flowers))
