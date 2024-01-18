parameter = 1000000

index = 0
maximum = 0

library = {}

def collatz(num):
    steps = 1
    
    while num > 1:
        if num in library.keys():
            steps += library[num] - 1
            break
        else:
            if num % 2 == 0:
                num /= 2
            else:
                num *= 3
                num += 1
            
            steps += 1
    
    return steps

for i in range(2, parameter):
    library[i] = collatz(i)
    
    if maximum < library[i]:
        maximum = library[i]
        index = i
    
    if (len(library) + 2) % int(parameter / 100) == 0:
        print((len(library) + 2) * 100 / parameter, end='')
        print("%")
    
print(str(index) + ": " + str(maximum))