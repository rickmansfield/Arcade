"""
since 1 ≤ n < 10^4.
area = ((1 - 1) x 4) + 1
area = ((2-1) x 4) + 1 =  5
area = ((3-1) x 4) + 5 = 13
area = ((4-1)) x 4) + 13 = 25
"""
"""
alternative
def shapeArea(n):
    # return (n*n)+((n-1)*(n-1))
"""

def shapeArea(n):
    count = 1
    for eachNum in range (1, n+1, 1):
        # print("eachNum", eachNum)
        count += ((eachNum-1)*4)
        # print("Count inside loop", count)
    return count
    
print(shapeArea(8000))