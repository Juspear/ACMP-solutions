# Decryption

A message of lowercase English letters and spaces is encrypted character by character:
letters get codes a = 1 … z = 26 and the space gets 27, the code is added to the character's
position in the message (starting from 1) modulo 27, and the result is written as a single
base-27 digit (`0`–`9`, `A`–`Q`). Decrypt the given string.

**Input** (`input.txt`): an encrypted string of 1 to 255 uppercase base-27 digits.
**Output** (`output.txt`): the decrypted message in lowercase.

Examples: `L7MO` → `test`, `576J9FLF` → `decoding`.

https://acmp.ru/index.asp?main=task&id_task=73
