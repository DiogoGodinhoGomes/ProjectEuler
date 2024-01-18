primes = [2]

final_factors = {}

for value in range(2, 21):
    i = 0
    
    num = value
    
    p_factors = {}
    
    while num > 1:
        if num % primes[i] == 0:
            num /= primes[i]
            
            if str(primes[i]) in p_factors:
                p_factors[str(primes[i])] += 1
            else:
                p_factors[str(primes[i])] = 1
        else:
            i += 1
            
            k = primes[-1] + 1
                    
            while i >= len(primes):
                prime = True
                
                for j in range(2, int(k/2) + 1):
                    if k % j == 0:
                        prime = False
                        break
                
                if prime:
                    primes.append(k)
                
                k += 1
    
    for key in p_factors.keys():
        if key in final_factors:
            final_factors[key] = max(p_factors[key], final_factors[key])
        else:
            final_factors[key] = p_factors[key]

print(final_factors)

total = 1

for key in final_factors:
    total *= pow(int(key), final_factors[key])
    
print(total)