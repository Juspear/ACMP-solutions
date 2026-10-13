# Railway cars

A train arrives with its cars numbered by a permutation of 1..N. The dispatcher may uncouple
the train at any places and rearrange the resulting blocks in any order, but cannot change the
order of cars inside a block or flip a block. Find the minimum number of couplings that must be
broken so the cars can be arranged in increasing order of their numbers.

**Input** (`input.txt`): the number N (1 ≤ N ≤ 100) and then the permutation of 1..N describing the arriving train.
**Output** (`output.txt`): the minimum number of couplings to break.

Examples: `4 / 3 1 2 4` → `2`, `5 / 5 4 3 2 1` → `4`, `2 / 1 2` → `0`.

https://acmp.ru/index.asp?main=task&id_task=246
