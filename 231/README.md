# String unpacking

A string of uppercase English letters is packed by replacing each run of repeated letters
with the run length followed by the letter (a single letter is left as is), so
`AAAABCCCCCDDDD` becomes `4AB5C4D`. Given a packed string, restore the original one and
print it split into lines of exactly 40 characters (the last line may be shorter).

**Input** (`input.txt`): one packed string of length 1 to 80 made of parts `nA` (2 ≤ n ≤ 99) or `A`.
**Output** (`output.txt`): the unpacked string, 40 characters per line.

Examples: `3A4B7D` → `AAABBBBDDDDDDD`, `95AB` → three lines: 40 `A`, 40 `A`, then 15 `A` and `B`.

https://acmp.ru/index.asp?main=task&id_task=231
