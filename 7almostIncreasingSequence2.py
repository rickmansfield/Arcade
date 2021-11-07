# import builtins
# import collections
# import math
# print(dir(builtins))
# print("-----------------")
# print(help(enumerate))

"""
U.P.E.R.
loop over the [input] array.integer sequence
for/while each i range(len(array) 
    remove i (temporarily) 
    if remaining array is sequential
        -ways to check seq... 
            -  < operator
        return true
    else 
        - replace value[i] 
        - and continue to next i 
return False
"""
def almostIncreasingSequence(sequence):
    if len(set(sequence)) == 1:
        True
    elif len(sequence) - len(set(sequence)) > 1:
        return False
    
    for i in range(len(sequence)-1):
        if sequence[i] < sequence[i+1]:
            continue
        el