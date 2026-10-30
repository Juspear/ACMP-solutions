# Rook game

A rook stands on a board that is infinite up and to the right. Two players take turns moving
it any nonzero number of cells down or left without leaving the board. Whoever moves it to
the corner (1, 1) wins. The first player must make at least one move; if he can't, the
winner is undefined. Both play optimally — who wins?

**Input** (`input.txt`): two positive integers X and Y (X, Y ≤ 10^9) — the starting cell.
**Output** (`output.txt`): `1` or `2` — the winner, or `0` if no move is possible.

Examples: `1 1` → `0`, `1 6` → `1`.

https://acmp.ru/index.asp?main=task&id_task=763
