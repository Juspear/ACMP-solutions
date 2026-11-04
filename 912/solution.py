from collections import Counter

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

counts = Counter(data[1:data[0] + 1])
best = max(counts.values())
leaders = [color for color, count in counts.items() if count == best]
answer = leaders[0] if len(leaders) == 1 else 0

with open("output.txt", "w") as f:
    f.write(f"{answer}\n")
