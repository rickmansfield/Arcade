# import builtins
# print(help(range))
# print(help(pU.sorted))
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
        product = inputArray[eachNumber] * inputArray[eachNumber +1]
        # if product > maxProd:
            # maxProd = product
        # print(products)
        pU.append(product)
    print("pU", pU)
    # # print(help(pU.sort))
    pU.sort()
    # print("pU", pU)
    return pU.pop() 

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))