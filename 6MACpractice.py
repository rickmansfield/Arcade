"""
this version of makeArracyConsecutive2() (MAC) is very 
mathy and should not be used if you want to be able to
convert your code to other languages. 
"""
def makeArrayConsecutive2(statues):
    print("max(statues)", max(statues))
    print("min(statues)", min(statues))
    return ((max(statues)-min(statues))+1)-len(statues)


print("results", makeArrayConsecutive2([6, 2, 3, 8])) # 3
# print(makeArrayConsecutive2([0, 3])) # 2
# print(makeArrayConsecutive2([5, 4, 6])) # 0 