days = list(map(int, open('input.txt').read().split()))
open('output.txt', 'w').write(str(sum(days) // 27))
