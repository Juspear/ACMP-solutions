# Parts

Two rigid parts lie on an N×M grid. In every row part A covers some leading cells and part B
covers some trailing cells (at least one each). Part B is slid to the left without rotation
until at least one of its cells touches part A. Find how many cells B moves.

**Input** (`input.txt`): N and M (1 ≤ N, M ≤ 100), then N rows of M characters `A`, `B` or `.`.
**Output** (`output.txt`): the shift distance.

Examples: `4 6 / AA.BBB / A....B / AAA..B / A..BBB` → `1`.

https://acmp.ru/index.asp?main=task&id_task=675
