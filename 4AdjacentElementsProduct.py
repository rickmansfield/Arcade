import numpy as np;

def adjMult(ar):
    r = []
    for n in range(len(ar)-1):
        m = ar[n] * ar[n+1]
        r.append(m)
        r.sort()
    return np.max(r)

print('Max value of the adjacent nums multiplied:', adjMult([3, 6, -2, -5, 7, 3]))

# Deatiled explaination---------------------------
"""
initiate an empty array "pU" (Products Unsorted) to capture the products of each pair
Iterate over the given array multiplying the current index value with the next (+1) index value and append that to the array. 
sort the final array "pS" (Products Sorted)
and return the last number at the final index. 
"""
def adjacentElementsProduct(inputArray):
    pU = []
    # maxProd = inputArray[0] * inputArray[1]
    # print(range(len(inputArray)))
    for eachNumber in range(len(inputArray)-1):
        product = inputArray[eachNumber] * inputArray[eachNumber + 1]
        # if product > maxProd:
        # maxProd = product
        # print(products)
        pU.append(product)
        # print("pU", pU)
        # # print(help(pU.sort))
        pU.sort()
        # print("pU", pU)
    return pU.pop()

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))

# another alternative answer without numpy------------------
def adjEl(arr):
    r = []
    for n in range(len(arr)-1):
        p = arr[n] * arr[n+1]
        r.append(p)
        r.sort()
    return r.pop()


print(adjEl([3, 6, -2, -5, 7, 3]))
