data = list(map(int, open('input.txt').read().split()))
gx, gy, dx, dy, n = data[:5]
ans = 'NO'
for k in range(n):
    x, y = data[5 + 2 * k], data[6 + 2 * k]
    g = (x - gx) ** 2 + (y - gy) ** 2
    d = (x - dx) ** 2 + (y - dy) ** 2
    if d >= 4 * g:
        ans = str(k + 1)
        break
open('output.txt', 'w').write(ans)
