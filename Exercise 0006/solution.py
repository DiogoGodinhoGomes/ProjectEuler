sum_a = 0
sum_b = 0

for i in range (1, 101):
    sum_a += i
    sum_b += i * i

sum_a *= sum_a

print(sum_a - sum_b)