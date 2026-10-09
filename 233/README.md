# Bus tour

A double-decker bus 437 cm tall drives along a route with N bridges. It can pass under a
bridge only if the bridge is strictly higher than the bus. Determine whether the tour ends
safely, and if not, at which bridge the bus crashes.

**Input** (`input.txt`): N (1 ≤ N ≤ 1000), then N bridge heights in route order (natural numbers up to 10000).
**Output** (`output.txt`): `No crash` if every bridge is passed, otherwise `Crash k`, where k is the number of the first bridge that is too low.

Examples: `1` / `763` → `No crash`, `3` / `763 245 113` → `Crash 2`, `1` / `437` → `Crash 1`.

https://acmp.ru/index.asp?main=task&id_task=233
