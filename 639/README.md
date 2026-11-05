# TopCoder

Contestants are split into rooms, and for every room the final standings are given in
non-increasing order of points. Merge all rooms into one overall standings table sorted by
points in non-increasing order (contestants with equal points may go in any order).

**Input** (`input.txt`): the number of rooms n (1 ≤ n ≤ 100); for each room the number of
contestants n_i (1 ≤ n_i ≤ 20) followed by n_i lines `points name`, where points is a real
number with two decimals (-5000 ≤ points ≤ 10000).
**Output** (`output.txt`): the total number of contestants, then the merged lines `points name`
with points printed with two decimals.

Examples: two rooms with 6 and 5 contestants → `11` followed by the merged table
(`909.94 Savior`, `867.15 Ying`, `448.12 natori`, ...).

https://acmp.ru/index.asp?main=task&id_task=639
