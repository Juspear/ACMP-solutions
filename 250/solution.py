with open('input.txt') as f:
    n = int(f.read().strip())


def twofold(x):
    return len(set(str(x))) <= 2


d = 0
while True:
    if n - d >= 1 and twofold(n - d):
        answer = n - d
        break
    if twofold(n + d):
        answer = n + d
        break
    d += 1

with open('output.txt', 'w') as f:
    f.write(str(answer) + '\n')
