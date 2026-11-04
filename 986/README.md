# Jumping journey

A grasshopper starts at point A1 and jumps through A2, ..., An in order. A frog sits at
point B and can reach anything within distance L, but only catches the grasshopper when it
has landed. Determine whether the grasshopper survives, or at which point it gets eaten
first.

**Input** (`input.txt`): N (1 ≤ N ≤ 10^5), the coordinates of B and L (0 ≤ L ≤ 5000), then N points Ai; all
coordinates are integers with absolute value up to 10^4.
**Output** (`output.txt`): `Yes` if the grasshopper is never caught, otherwise the index of the first point where it
is eaten.

Examples: `3 0 0 1` / `2 0` / `1 1` / `0 1` → `3`, `2 0 0 100` / `1 1` / `2 2` → `1`,
`3 0 0 1` / `1 1` / `2 2` / `3 3` → `Yes`.

https://acmp.ru/index.asp?main=task&id_task=986
