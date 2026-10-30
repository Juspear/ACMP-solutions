# Compressing binary strings

A binary string is compressed by reading it left to right and replacing `1` with `a`,
`01` with `b`, `001` with `c`, and so on up to 25 zeros followed by `1`, which becomes `z`.
Output the compressed form of the given string.

**Input** (`input.txt`): a string of `0` and `1`, length 1 to 255; it is guaranteed to be compressible.
**Output** (`output.txt`): the compressed string of lowercase letters.

Examples: `101` → `ab`, `101001` → `abc`, `0000000000000000000000001` → `y`.

https://acmp.ru/index.asp?main=task&id_task=950
