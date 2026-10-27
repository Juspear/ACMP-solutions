# Left recursion

A context-free grammar is given as a list of production rules of the form `A->R`, where the
left side is a single nonterminal (an uppercase letter) and the right side is a string of
terminals (lowercase letters) and nonterminals. A rule has immediate left recursion if the
right side starts with the same nonterminal that stands on the left. Count such rules.

**Input** (`input.txt`): the number of rules n (1 ≤ n ≤ 1000), then n rules, one per line.
**Output** (`output.txt`): the number of rules with immediate left recursion.

Examples: `3 / S->Sabc / S->A / A->AA` → `2`.

https://acmp.ru/index.asp?main=task&id_task=387
