data = list(map(int, open("input.txt").read().split()))
n = data[0]
sockets = data[1:n + 1]
open("output.txt", "w").write(str(sum(sockets) - (n - 1)))
