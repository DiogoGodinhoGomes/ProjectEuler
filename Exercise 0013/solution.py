numbers = []

with open("numbers.txt") as file:    
    for line in file:
        new_line = line.strip()
        
        numbers.append(int(new_line))

print(str(sum(numbers))[:10])