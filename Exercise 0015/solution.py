import math as mt

def combi(n, p):
    return int(mt.factorial(n)/mt.factorial(p)/mt.factorial(n - p))

for i in range(1, 21):
    print(str(i) + ": " + str(combi(i * 2, i)))