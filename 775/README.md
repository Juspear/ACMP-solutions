# Collatz problem

In the Collatz process a number is halved if it is even, otherwise it is replaced by 3N+1,
and this repeats until the number becomes 1. Vasily believes that Mersenne numbers (2^n - 1)
reach 1 faster than others. Given a Mersenne number N and a segment length M, find a number K
with N < K ≤ N+M that reaches 1 in fewer steps than N. If several exist, choose the fastest one,
and among equally fast ones the smallest.

**Input** (`input.txt`): integers N (3 ≤ N ≤ 10^100, a Mersenne number) and M (0 ≤ M ≤ 10^100).
**Output** (`output.txt`): the number K, or `NO` if there is none.

Examples: `3 5` → `4`.

https://acmp.ru/index.asp?main=task&id_task=775
