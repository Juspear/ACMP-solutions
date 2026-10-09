from decimal import Decimal, ROUND_HALF_UP

E = Decimal("2.7182818284590452353602875")

with open("input.txt") as f:
    n = int(f.read())

value = E.quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP)

with open("output.txt", "w") as f:
    f.write(f"{value}\n")
