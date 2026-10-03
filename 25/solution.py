with open('input.txt') as f:
    a, b = map(int, f.read().split())

if a < b:
    sign = '<'
elif a > b:
    sign = '>'
else:
    sign = '='

with open('output.txt', 'w') as f:
    f.write(sign)
