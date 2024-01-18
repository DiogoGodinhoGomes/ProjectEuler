def determine_limit(power):
    i = 0

    n = "0"

    while int(n) <= i * pow(9, power):
        if i > 0:
            n += '9'
        
        i += 1

    return int(n) + 1

value = 0

total = 0

power = 5

results = []

limit = determine_limit(power)

for value in range(limit):
    total = 0
    
    for d in str(value):
        total += pow(int(d), power)
    
    if value == total and len(str(value)) > 1:
        results.append(value)

print(sum(results))