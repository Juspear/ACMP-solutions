with open('input.txt') as f:
    data = f.read().split()

n = int(data[0])
times = list(map(int, data[1:n + 1]))


def result(order):
    cur = 0
    count = 0
    penalty = 0
    for x in order:
        cur += x
        if cur <= 300:
            count += 1
            penalty += cur
    return count, penalty


fifth = result(times)
third = result(times[::-1])
first = result(sorted(times))

options = [
    (fifth[0], fifth[1], 5),
    (third[0], third[1], 3),
    (first[0], first[1], 1),
]
winner = min(options, key=lambda o: (-o[0], o[1], o[2]))

with open('output.txt', 'w') as f:
    f.write(str(winner[2]))
