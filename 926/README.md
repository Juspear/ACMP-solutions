# Cities - 2

An N × N board has some cells marked as cities, and the total number of cities is even.
Split all cells of the board between two states so that each state is connected (cells
are adjacent when they share a side) and both states contain the same number of cities.
Any valid split may be printed.

**Input** (`input.txt`): N (N ≤ 50), then N rows of N letters: `C` is a city, `D` is an empty cell.
**Output** (`output.txt`): N rows of N digits, `1` or `2`, showing which state each cell belongs to.

Examples: `3 / DDD DDC DDC` → `222 212 211`, `5 / DDDDD CDCDC DCCDC DDDDD DDDDD` → `11111 12221 12221 11111 11111`.

https://acmp.ru/index.asp?main=task&id_task=926
