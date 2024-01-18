minimum = 2

maximum = 100

results = set()

for a in range(minimum, maximum + 1):
    for b in range(minimum, maximum + 1):
        results.add(pow(a, b))

print(len(results))