# Amdahl's law

There are n processors, and p percent of the computation cannot be parallelized, while
the rest is split evenly among all processors. Find how many times faster the whole
computation runs compared to a single processor.

**Input** (`input.txt`): two integers n and p (1 ≤ n ≤ 1000, 0 ≤ p ≤ 100).
**Output** (`output.txt`): the speedup with precision of at least 10^-6.

Examples: `10 50` → `1.818181818`, `10 25` → `3.076923077`, `1000 100` → `1.000000000`.

https://acmp.ru/index.asp?main=task&id_task=439
