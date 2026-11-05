# Keyboard - 2

Each of the N keys of a keyboard can withstand a certain number of presses c_i; pressing it
more times than that breaks it. Given the sequence of K pressed keys, determine which keys
end up broken.

**Input** (`input.txt`): N (1 ≤ N ≤ 100), then N limits c_i (1 ≤ c_i ≤ 100000), then K
(1 ≤ K ≤ 100000), then K key numbers p_j (1 ≤ p_j ≤ N).
**Output** (`output.txt`): N lines, `yes` if the i-th key broke and `no` otherwise.

Examples: `5 / 1 50 3 4 3 / 16 / 1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5` → `yes no no no yes`.

https://acmp.ru/index.asp?main=task&id_task=534
