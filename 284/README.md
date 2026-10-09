# Subarray of an array

Given an array a1..an, the subarray f(i, j) consists of the elements ai, ai+1, ..., aj.
Answer m queries, printing the requested subarray for each one.

**Input** (`input.txt`): n (1 ≤ n ≤ 1000), then n integers in the 32-bit signed range, then m (1 ≤ m ≤ 100), then m pairs i, j (1 ≤ i ≤ j ≤ n).
**Output** (`output.txt`): for each pair, the subarray f(i, j) on its own line.

Examples: `6` / `1 2 3 4 5 6` / `5` / `1 1` / `2 6` / `3 4` / `5 6` / `2 4` → `1` / `2 3 4 5 6` / `3 4` / `5 6` / `2 3 4`.

https://acmp.ru/index.asp?main=task&id_task=284
