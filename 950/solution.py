s = open('input.txt').read().strip()
res = []
zeros = 0
for ch in s:
    if ch == '0':
        zeros += 1
    else:
        res.append(chr(ord('a') + zeros))
        zeros = 0
open('output.txt', 'w').write(''.join(res))
