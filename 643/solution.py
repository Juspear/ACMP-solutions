n = int(open('input.txt').read())
open('output.txt', 'w').write(str(n + bin(n).count('1')))
