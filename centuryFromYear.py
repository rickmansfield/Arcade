def centuryFromYear(year):
    # return 1+ (year-1) //100
    century = 1 + (year-1) //100
    return century
    # print("year -1", year)
    
print(centuryFromYear(1905))
print(centuryFromYear(1))
print(centuryFromYear(2005))
print(centuryFromYear(1700))

