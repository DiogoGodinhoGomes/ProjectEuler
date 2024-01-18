def prepare_binaries(n):
    binaries = [""]

    for i in range(n):
        binaries += binaries
        
        for i in range(len(binaries)):
            if i < len(binaries) / 2:
                binaries[i] += "0"
            else:
                binaries[i] += "1"
    
    return binaries

matrix = []

with open("code.txt") as code:
    for line in code:
        array = []
        
        for n in line.split():
            array.append(int(n))
        
        matrix.append(array)

binaries = prepare_binaries(len(matrix) - 1)

totals = []

for b in range(len(binaries)):
    j = 0
    
    total = matrix[0][j]
    
    for i, elem in enumerate(binaries[b]):
        j += int(binaries[b][i])
        
        total += matrix[i + 1][j]
    
    totals.append(total)

print(max(totals))