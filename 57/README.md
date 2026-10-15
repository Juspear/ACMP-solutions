# Computer network

N houses must be connected to the network: a wire goes from the connection point to one
house, and from that house separate wires go to every other house. A unit of wire costs c and the
budget is p. Decide whether the budget is enough for the cheapest such layout.

**Input** (`input.txt`): N, c and p (1 ≤ N ≤ 1000, 0 ≤ c ≤ 10^4, 0 ≤ p ≤ 10^15), N lines with house coordinates, then the coordinates of the connection point (all at most 1000 in absolute value).
**Output** (`output.txt`): `YES` if the money is enough, otherwise `NO`.

Examples: `3 2 6 / 0 0 / 1 0 / 0 1 / -1 0` → `YES`, `3 1 5 / 1 1 / 2 2 / 3 3 / 4 4` → `NO`.

https://acmp.ru/index.asp?main=task&id_task=57
