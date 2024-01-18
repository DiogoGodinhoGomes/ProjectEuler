num = 1000000

possibilities = "0123456789"

results = []

for i in range(len(possibilities)):
    if len(results) == 0:
        results.append(possibilities[0])
    else:
        size = len(results)
        
        results = results * (i + 1)
        
        for j in range(len(results)):
            pos = int(j / size)
            
            results[j] = results[j][:pos] + possibilities[i] + results[j][pos:]

results = sorted(results)

assert(len(results) == len(set(results)))

print(len(results), results[num - 1])