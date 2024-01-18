def write_primes(limit):
    num = 3

    primes = [2]

    while len(primes) < limit:
        prime = True
        
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                prime = False
                break
        
        if prime:
            primes.append(num)
        
        num += 1

    with open("primes.txt", "w") as file:
        for i, prime in enumerate(primes):
            file.write(str(i) + ": " + str(prime) + "\n")