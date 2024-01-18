num = 2

primes = []

while len(primes) < 10002:
    prime = True
    
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        primes.append(num)
    
    num += 1

    print(len(primes))

print(primes)