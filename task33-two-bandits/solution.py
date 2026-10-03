with open('input.txt') as f:
    harry, larry = map(int, f.read().split())

with open('output.txt', 'w') as f:
    f.write(f'{larry - 1} {harry - 1}')
