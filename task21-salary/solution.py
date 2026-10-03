with open('input.txt') as f:
    salaries = list(map(int, f.read().split()))

with open('output.txt', 'w') as f:
    f.write(str(max(salaries) - min(salaries)))
