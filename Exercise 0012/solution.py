def prepare_binaries(n):
    binaries = [""]

    for i in range(n):
        binaries += binaries
        
        for i in range(len(binaries)):
            if i < len(binaries) / 2:
                binaries[i] += "0"
            else:
                binaries[i] += "1"
    
    return binaries

def find_factors(num):
    i = 0
    
    p_list = []

    while num > 1:
        if num % primes[i] == 0:
            num /= primes[i]
            
            p_list.append(primes[i])
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

    return p_list

def num_divisors(p_list):
    set_divisors = set()

    for i in range(pow(2, len(p_list))):
        total = 1
        
        for index, elem in enumerate(binaries[i][:len(p_list)]):
            total *= p_list[index] if int(elem) == 1 else 1
        
        set_divisors.add(total)
    
    return len(set_divisors)

primes = [2]

binaries = prepare_binaries(20)

number = 0
maximum = 0
increment = 1

while maximum <= 500:
    number += increment
    
    maximum = max(maximum, num_divisors(find_factors(number)))
    
    increment += 1

print(number)