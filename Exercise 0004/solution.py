palindromes = []

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        number = str(i * j)
        
        palindrome = True
        
        for k in range(int(len(number) / 2)):
            if number[k] != number[-(k + 1)]:
                palindrome = False
        
        if palindrome:
            
            palindromes.append(int(number))

palindromes.sort(reverse = True)

print(max(palindromes))