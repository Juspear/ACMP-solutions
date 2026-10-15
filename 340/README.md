# Boxes

There are two boxes with sizes A1 × B1 × C1 and A2 × B2 × C2. Boxes may be rotated by 90 degrees
around any edge. Determine whether one of them fits into the other.

**Input** (`input.txt`): A1 B1 C1 on the first line and A2 B2 C2 on the second (positive, ≤ 1000).
**Output** (`output.txt`): `Boxes are equal` if the boxes are the same, `The first box is smaller than the second one`
if the first fits into the second, `The first box is larger than the second one` if the second fits into the first,
and `Boxes are incomparable` otherwise.

Examples: `1 2 3 / 3 2 1` → `Boxes are equal`, `2 2 3 / 3 2 1` → `The first box is larger than the second one`,
`2 2 3 / 3 2 3` → `The first box is smaller than the second one`, `3 4 5 / 2 4 6` → `Boxes are incomparable`.

https://acmp.ru/index.asp?main=task&id_task=340
