coins = [1, 2, 5, 10, 20, 50, 100, 200]

index = 0

quantity = 200

possibilities = 0

coin = len(coins) - 1

while coin >= 0:
    total = quantity
    
    while total > 0:
        if total - coins[coin] >= 0:
            total -= coins[coin]
            
            if total == 0:
                possibilities += 1
                
                coin -= 1
        else:
            coin -= 1



'''
sets = set()

current = [0] * len(coins)

current[index] = int(quantity / coins[index])

sets.append(current)

while index < len(coins):
    current[index] = int(quantity / coins[index])
    
    for i in 
    
    sets.append(current)
    
    index += 1
'''