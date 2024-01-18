i = 2

first = 1

second = 1

while len(str(second)) < 1000:
    third = first + second
    
    first = second
    
    second = third
    
    i += 1

print(i, len(str(third)))