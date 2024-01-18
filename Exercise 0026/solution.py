import functions as fc

prec = 10000

number = 1000

index, maximum, dtnr = fc.get_all_periods(prec, number)

print(index, "->", maximum)