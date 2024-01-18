import time as tm

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

start_time = tm.time()

num = 28123

primes = [2]

binaries = prepare_binaries(14)

abundant = []

for i in range(2, num + 1):
    sum_d = sum(num_divisors(find_factors(i)))
    
    if i < sum_d:
        abundant.append(i)

can_be_sum = set()

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        total = abundant[i] + abundant[j]
        
        if total <= num:
            can_be_sum.add(total)

can_be_sum = list(can_be_sum)

cannot_be_sum = set()

for i in range(1, num + 1):
    if i not in can_be_sum:
        cannot_be_sum.add(i)

cannot_be_sum = list(cannot_be_sum)

print(sum(cannot_be_sum), "---", tm.time() - start_time, "s")