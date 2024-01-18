import time as tm

maximum = 2000000

total = 0

num = 2

i_time = tm.time()

while num < maximum:    
    if num % 2000 == 0:
        print(str(num * 100 / maximum ), end='')
        print("% - " + str(tm.time() - i_time))
    
    prime = True
    
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        total += num
    
    num += 1

print(total)