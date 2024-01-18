from decimal import Decimal, getcontext

def get_factors(num, primes):
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

    return p_list, primes

def get_digits(prec, d):      
    getcontext().prec = prec + 1

    fraction = Decimal('1') / Decimal(d)

    digits = []

    for i in range(prec):
        digit = int(fraction * 10)
        
        fraction *= 10
        
        fraction -= digit
        
        digits.append(digit)
        
        if fraction == 0:
            digits = []
            
            break

    return digits

def get_period(prec, number):
    digits = get_digits(prec, number)
    
    period = []
    
    period_length = 1
    
    pattern_found = False
    
    while not pattern_found and period_length <= int(len(digits) / 2):
        period = digits[:period_length]
        
        if period == digits[period_length : 2 * period_length]:        
            possible_length = len(digits[: -(len(digits) % number)])
            
            match = 1
            
            for i in range(int(possible_length / number)):
                if period != digits[i * period_length : (i + 1) * period_length]:
                    match *= 0
            
            if match == 1:
                pattern_found = True
        
        period_length += 1
        
    return period

def get_all_periods(prec, number):
    dtnr = {}
    
    index = 0
    
    maximum = 0

    for i in range(1, number + 1):
        num = i
        
        while num % 2 == 0:
            num /= 2
        
        while num % 5 == 0:
            num /= 5
        
        mult = i / num
        
        period = get_period(prec, int(i / mult))
        
        dtnr[i] = len(period)
        
        if len(period) >= maximum:
            index = i
            maximum = len(period)

    return index, maximum, dtnr