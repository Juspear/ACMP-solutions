with open('input.txt') as f:
    words = f.read().split()

n = int(words[0])
gods = words[1:n + 1]
m = int(words[n + 1])
suspicious = words[n + 2:n + 2 + m]


def one_mistake(a, b):
    return len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1


counts = [sum(one_mistake(god, word) for word in suspicious) for god in gods]

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, counts)) + '\n')
