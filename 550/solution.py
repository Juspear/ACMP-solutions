year = int(open("input.txt").read())
leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
day = 12 if leap else 13
open("output.txt", "w").write(f"{day}/09/{year:04d}")
