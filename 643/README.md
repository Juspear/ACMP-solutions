# Time key

An activation key changes every minute: if it is N now, a minute later it becomes N + S(N),
where S(N) is the number of ones in the binary representation of N. Given the current key,
output the next one.

**Input** (`input.txt`): one integer N (1 ≤ N ≤ 2·10^9).
**Output** (`output.txt`): the key value one minute later.

Examples: `2` → `3`, `6` → `8`, `27` → `31`.

https://acmp.ru/index.asp?main=task&id_task=643
