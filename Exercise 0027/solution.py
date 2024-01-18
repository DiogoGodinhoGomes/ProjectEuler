import numpy as np
import functions as fc

# fc.write_primes(10000)

num = 999

primes = []

b_range = []

with open("primes.txt") as file:
    for line in file:
        primes.append(int(line.replace(":","").split()[1]))

i = 0

while primes[i] < num:
    b_range.append(primes[i])
    
    i += 1

b_range = sorted(np.array(b_range) * (-1)) + b_range

a_max = 0
b_max = 0
n_max = 0

for a in range(-num, num + 1):
    for b in b_range:
        n = 0
        
        while n * n + a * n + b in primes:
            n += 1
        
        if n > 0:
            print(a, b, n, n_max)
            
            if n > n_max:
                a_max = a
                b_max = b
                n_max = n

print(a_max, b_max, n_max)