def is_leap(year):
    if year % 4 != 0:
        is_leap = False
    else:
        if year % 400 == 0:
            is_leap = True
        elif year % 100 == 0:
            is_leap = False
        else:
            is_leap = True
    
    return is_leap

def get_years():
    weeks = [1, 0, 0, 0, 0, 0, 0] * 54
    
    month = [1] + [0] * 30
    
    leap_months = [0, -2, 0, -1, 0, -1, 0, 0, -1, 0, -1, 0]
    common_months = [0, -3, 0, -1, 0, -1, 0, 0, -1, 0, -1, 0]

    leap = []
    common = []

    for elem in leap_months:
        leap += month if elem == 0 else month[:elem]

    for elem in common_months:
        common += month if elem == 0 else month[:elem]
    
    return weeks, month, leap, common

weeks, month, leap, common = get_years()

rest = 1

count = 0

for year in range(1900, 2001):
    if year == 1901:
        count = 0
    
    m_year = leap if is_leap(year) else common
    
    leng = len(m_year)
    
    w_year = weeks[rest : leng + rest]
    
    for i in range(leng):
        count += m_year[i] * w_year[i]
    
    rest = (rest + leng) % 7

print(count)