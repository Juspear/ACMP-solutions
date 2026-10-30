data = list(map(int, open('input.txt').read().split()))
n, s = data[0], data[1]
prices = sorted(data[2:2 + n])
cnt = 0
for p in prices:
    if p > s:
        break
    s -= p
    cnt += 1
open('output.txt', 'w').write(str(cnt))
