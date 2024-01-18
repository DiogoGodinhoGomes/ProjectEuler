length = 4

matrix = []
values = []

with open("matrix.txt") as file:    
    for line in file:
        new_line = line.strip().split()
        
        matrix += [new_line]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j + length - 1 < len(matrix[i]) and i + length - 1 < len(matrix):
            temp = 1
            
            for k in range(length):
                temp *= int(matrix[i + k][j + k])
            
            values.append(temp)
        
        if j + length - 1 < len(matrix[i]) and i + 1 - length >= 0:
            temp = 1
            
            for k in range(length):
                temp *= int(matrix[i - k][j + k])
            
            values.append(temp)

        if j + length - 1 < len(matrix[i]):
            temp = 1
            
            for k in range(length):
                temp *= int(matrix[i][j + k])
            
            values.append(temp)
        
        if i + length - 1 < len(matrix):
            temp = 1
            
            for k in range(length):
                temp *= int(matrix[i + k][j])
            
            values.append(temp)

print(max(values))