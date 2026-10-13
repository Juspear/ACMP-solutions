with open('input.txt') as f:
    number = f.read().strip()

steps = 0
while len(number) > 1:
    number = str(sum(int(c) for c in number))
    steps += 1

with open('output.txt', 'w') as f:
    f.write(f'{number} {steps}\n')
