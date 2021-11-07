"""
WARNING this doesn't pass all edge cases. 
"""
def canMakeTriangle(arr):
    result = []
    for i in range(0, len(arr)-2, 1):
        print(arr[i])
        if arr[i] + arr[i+1] > arr[i+2]:
            result.append(1)
        elif arr[i] + arr[i+2] > arr[i+1]:
            result.append(1)
        elif arr[i+1] + arr[i+2] >arr[i]:
            result.append(1)
        else:
            result.append(0)
    return result