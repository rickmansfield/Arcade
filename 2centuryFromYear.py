def centuryFromYear(year):
    return 1+ (year-1) //100
    # century = 1 + ((year-1) // 100)
    # return century
    
print(centuryFromYear(1905))
print(centuryFromYear(1))
print(centuryFromYear(2005))
print('That year is in the', centuryFromYear(1700),'th century')

# use floor division to solve this "//"
# Modulo gives you the remainer but floor division gives you the other number not the remainder. 
# remember this "/" is float division 
# note how subtracting 1 from any year that does't end in 00 doesn't hurt any thing or change the results. But when you subtract 1 from a turn of the century number ending in 00 then it ensures your answer produces the correct century. For example 1700-1 = 1699 and when you floor divide 1699 you get 16 hence adding back +1 now returns the "17th" century
# 