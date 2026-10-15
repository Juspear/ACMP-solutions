# Score counting

A solution is checked on N tests with given costs, and passing all tests gives an extra
bonus. Each attempt i is penalized by 2·(i−1) points, and the participant's result is the best
penalized score over all attempts so far. Output the result after each attempt.

**Input** (`input.txt`): N (1 ≤ N ≤ 100), N test costs, the bonus (0..100), M (1 ≤ M ≤ 100), then M lines of N zeros/ones — which tests each attempt passed.
**Output** (`output.txt`): M numbers — the result after the first i attempts.

Examples: `4 / 1 2 3 4 / 5 / 3 / 0 0 0 0 / 1 1 1 1 / 0 1 0 1` → `0 / 13 / 13`.

https://acmp.ru/index.asp?main=task&id_task=213
