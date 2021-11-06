def almostIncreasingSequence(sequence):
    s = sequence
    s2 = s[:]
    deleted = 0
    if (len(s) - len(set(s))) > 1:
        return False
    elif len(set(s)) == 1:
        return True
    
    for i in range(len(s)-1):
        if s2[i] < s2[i+1]:
            continue
        else:
            del s[i:i+2]
            deleted += 1
            
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
        
    if deleted > 1:
        return False
    else:
        return True
print(almostIncreasingSequence([1, 2, 1, 3, 4]))
# print(almostIncreasingSequence("1, 2, 3, 4"))