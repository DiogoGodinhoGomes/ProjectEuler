import time as tm

num = 1

total = 0

max_num_dvsr = 1

i_time = tm.time()

while max_num_dvsr < 500:
    total += num
    
    num_dvsrs = 1
    
    for i in range(1, int(total/2) + 1):
        if total % i == 0:
            num_dvsrs += 1
    
    if num_dvsrs > max_num_dvsr:
        print(str(num) + ": " + str(total) + " --- " + str(num_dvsrs) + " (" + str(tm.time() - i_time) + "s)")
    elif num % 1000 == 0:
        print(str(num) + ": (" + str(tm.time() - i_time) + "s)")
    
    max_num_dvsr = max(max_num_dvsr, num_dvsrs)
    
    num += 1