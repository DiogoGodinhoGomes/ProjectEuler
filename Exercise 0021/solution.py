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
    
    divisors = sorted(list(set_divisors))
    
    divisors.pop(-1)
    
    return divisors

num = 10000

primes = [2]

binaries = prepare_binaries(20)

results = dict()

for number in range(2, num):
    results[number] = sum(num_divisors(find_factors(number)))

amic = set()

keys = list(results.keys())

for i in range(num - 2):
    a = keys[i]
    b = results[i + 2]
    
    if b - 2 >= 0 and b < num:
        if a != b and results[b] == a:
            amic.add(a)
            amic.add(b)

print(sum(sorted(amic)))