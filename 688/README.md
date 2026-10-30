# Gopher and dog

A gopher and a dog are on a field with several holes. The gopher runs in a straight line to
some hole, and the dog guesses the hole and runs straight to it twice as fast. If the dog
gets there strictly earlier, the gopher is eaten. Find a hole where the gopher is safe.

**Input** (`input.txt`): gopher coordinates, dog coordinates, the number of holes n (n ≤ 1000)
and then n lines with hole coordinates (integers, |coord| ≤ 10000).
**Output** (`output.txt`): the index of the first safe hole in input order, or `NO`.

Examples: gopher `10 10`, dog `20 20`, hole `15 15` → `NO`;
gopher `20 20`, dog `10 10`, holes `15 15`, `25 25` → `2`.

https://acmp.ru/index.asp?main=task&id_task=688
