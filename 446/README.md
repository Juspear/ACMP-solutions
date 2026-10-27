# Scoreboard

A rectangular n × m scoreboard has to show an n × m picture where every cell is red (R),
green (G), blue (B) or black (.). Each scoreboard cell can always show black, and in addition
a subset of the three base colors encoded as a number from 0 to 7: bit 4 is red, bit 2 is
green, bit 1 is blue. Decide whether the picture can be displayed.

**Input** (`input.txt`): n and m (1 ≤ n, m ≤ 100), then n rows of the picture, then n rows of m numbers describing the scoreboard cells.
**Output** (`output.txt`): `YES` if the picture can be shown, otherwise `NO`.

Examples: the picture `.GB / R.B / RG.` on the board `0 1 2 / 3 4 5 / 6 7 0` → `NO`, the picture `RGB / .G.` on a board of all 7s → `YES`.

https://acmp.ru/index.asp?main=task&id_task=446
