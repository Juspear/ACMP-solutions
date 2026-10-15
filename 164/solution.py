with open('input.txt') as f:
    ticket = f.read().strip()


def root(s):
    total = sum(int(c) for c in s)
    return 0 if total == 0 else 1 + (total - 1) % 9


lucky = any(root(ticket[:i]) == root(ticket[i:]) for i in range(1, len(ticket)))

with open('output.txt', 'w') as f:
    f.write('YES\n' if lucky else 'NO\n')
