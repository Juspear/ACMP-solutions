# Campfire

Joe lights a fire at time 0 and has n logs with known burning times. He may throw any
number of logs at once, and logs ignite instantly. To keep the fire alive, if the last log
burns out at time t, the next one must be thrown in no later than t - 1. All n logs must
be used. Determine whether the fire can burn for exactly m minutes.

**Input** (`input.txt`): n and m (1 ≤ n ≤ 100, 1 ≤ m ≤ 1000), then n burning times ai (2 ≤ ai ≤ 1000).
**Output** (`output.txt`): `yes` if it is possible, `no` otherwise.

Examples: `3 7` / `2 3 5` → `yes`, `2 5` / `3 9` → `no`, `4 10` / `3 3 3 3` → `no`.

https://acmp.ru/index.asp?main=task&id_task=285
