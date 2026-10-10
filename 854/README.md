# Air conditioner

An air conditioner has a target temperature and one of four modes: `freeze` can only lower the
temperature, `heat` can only raise it, `auto` can do both, and `fan` does not change it at all.
In one hour it brings the room to the target temperature whenever its mode allows. Given the room
temperature, the target temperature and the mode, find the room temperature after one hour.

**Input** (`input.txt`): the first line has two integers troom and tcond (−50 ≤ troom, tcond ≤ 50), the second line has the mode in lowercase letters.
**Output** (`output.txt`): the temperature in the room after one hour.

Examples: `10 20 / heat` → `20`, `10 20 / freeze` → `10`.

https://acmp.ru/index.asp?main=task&id_task=854
