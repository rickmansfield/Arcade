def sa(n):
    count = 1
    for n in range(1, n+1, 1):
        count += ((n-1)*4)
    return count

print('answer:', sa(1)); # 1
print('answer:', sa(2)); # 5
print('answer:', sa(3)) # 13
print(sa(8000)) # 127984001
