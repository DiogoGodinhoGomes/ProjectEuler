import numpy as np

length = 13

results = []

with open("number.txt") as number:
    sequence = []
    
    for line in number:
        new_line = line.strip()
        
        sequence += new_line

i = 0

while i + length < len(sequence):
    name = ""
    total = 1
    
    for j in range(length):
        name += sequence[i + j]
        total *= int(sequence[i + j])
    
    results.append([int(name), int(total)])
    
    i += 1

final = np.array(results)

print(max(final[:,1]))