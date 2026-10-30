lines = open('input.txt').read().split('\n')
lines = [line.rstrip('\r') for line in lines]
team = lines[0]
names = sorted(lines[1:4])
open('output.txt', 'w').write(team + ': ' + ', '.join(names))
