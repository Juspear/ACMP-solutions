x, y = map(int, open('input.txt').read().split())
if x == 1 and y == 1:
    ans = 0
elif x == y:
    ans = 2
else:
    ans = 1
open('output.txt', 'w').write(str(ans))
