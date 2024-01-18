maximum = 1001

index = 1

total = 1

temp = 1

add = 0

while temp < pow(maximum, 2):    
    add += 2
    
    for i in range(4):
        temp += add
        
        total += temp
    
    index += 2
    
    assert(temp == pow(index, 2))

print(total)