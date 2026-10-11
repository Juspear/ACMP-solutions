with open("input.txt") as f:
    move = f.readline().strip()

def valid(cell):
    return cell[0] in "ABCDEFGH" and cell[1] in "12345678"

if len(move) != 5 or move[2] != "-" or not valid(move[:2]) or not valid(move[3:]):
    answer = "ERROR"
else:
    dx = abs(ord(move[0]) - ord(move[3]))
    dy = abs(ord(move[1]) - ord(move[4]))
    answer = "YES" if {dx, dy} == {1, 2} else "NO"

with open("output.txt", "w") as f:
    f.write(answer)
