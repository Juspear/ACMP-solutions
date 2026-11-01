# Kaprekar's constant

Take a four-digit number whose digits are not all equal. Arrange its digits in descending
order, then in ascending order, and subtract the smaller number from the larger one.
Repeat the operation with the difference, padding it with leading zeros to four digits
when needed. Eventually the process reaches a number that maps to itself, Kaprekar's
constant. Find this constant and the number of steps needed to reach it.

**Input** (`input.txt`): a four-digit number.
**Output** (`output.txt`): the constant on the first line and the number of steps on the second.

Examples: `1234` → `6174` and `3`.

https://acmp.ru/index.asp?main=task&id_task=457
