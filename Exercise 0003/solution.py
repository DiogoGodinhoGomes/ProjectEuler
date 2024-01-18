i = 0

num = 600851475143

primes = [2]

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

print(p_factors)