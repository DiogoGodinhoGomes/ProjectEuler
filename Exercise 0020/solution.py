import math as mt

number = str(mt.factorial(100))

total = 0

for i in number:
    total += int(i)

print(total)