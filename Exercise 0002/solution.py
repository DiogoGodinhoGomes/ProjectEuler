fibo = [1, 2]

while fibo[-2] + fibo[-1] < 4000000:
    fibo.append(fibo[-2] + fibo[-1])

total = 0

for i in fibo:
    if i % 2 == 0:
        total += i;

print(total)