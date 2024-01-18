parameter = 1000

length = 4

array = [''] * length

num_dict = { '0' : "zero",
             '1' : "one",
             '2' : "two",
             '3' : "three",
             '4' : "four",
             '5' : "five",
             '6' : "six",
             '7' : "seven",
             '8' : "eight",
             '9' : "nine",
             '10' : "ten",
             '11' : "eleven",
             '12' : "twelve",
             '13' : "thirteen",
             '14' : "fourteen",
             '15' : "fifteen",
             '16' : "sixteen",
             '17' : "seventeen",
             '18' : "eighteen",
             '19' : "nineteen",
             '20' : "twenty",
             '30' : "thirty",
             '40' : "forty",
             '50' : "fifty",
             '60' : "sixty",
             '70' : "seventy",
             '80' : "eighty",
             '90' : "ninety" }

def num_letters(n):
    num = str(n)
    
    for i in range(length):
        if i < len(num):
            array[-(i + 1)] = num[-(i + 1)]
        else:
            array[-(i + 1)] = '0'
    
    words = ""
    
    if array[0] != '0':
        words += num_dict[array[0]] + "thousand"
    
    if array[1] != '0':
        words += num_dict[array[1]] + "hundred"
    
    if (array[0] != '0' or array[1] != '0') and (array[2] != '0' or array[3] != '0'):
        words += "and"
        
    dec = int(array[-2] + array[-1])
    
    if dec > 0 and dec < 20:
        words += num_dict[str(dec)]
    elif dec > 0:
        new_dec = int(dec / 10) * 10
        
        words += num_dict[str(new_dec)]
        
        if array[3] != '0':
            words += num_dict[array[3]]
    
    return len(words)

total = 0

for i in range(1, parameter + 1):
    total += num_letters(i)

print(total)