found = False

a = 0

while a < 1000 and not found:
    a += 1
    
    b = a - 1
    
    while b < 1000 and not found:
        b += 1
        
        c = b - 1
        
        while c < 1000 and not found:
            c += 1
            
            if a % 10 == 0 and b % 100 == 0 and c % 1000 == 0:
                print("Checking (" + str(a) + ", " + str(b) + ", " + str(c) + ")...")
                
            if a * a + b * b == c * c and a + b + c == 1000:
                found = True

print("(a, b, c) = (" + str(a) + ", " + str(b) + ", " + str(c) + ")!")

print(a * b * c)