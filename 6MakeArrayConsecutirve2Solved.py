"""
Alternative. Not advise unless you are math oriented. 

def makeArrayConsecutive2(statues):
return (max(statues)-min(statues)+1)-len(statues)

print(makeArrayConsecutive2([6, 2, 3, 8])) # 3
print(makeArrayConsecutive2([0, 3])) # 2
print(makeArrayConsecutive2([5, 4, 6])) # 0 
"""
def makeArrayConsecutive2(statues):
    statues.sort()
    sorted_statues = sorted(statues)
    output = []
    statues_size = sorted_statues[0]
    print("sorted_statues", sorted_statues)
    
    while statues_size != sorted_statues[-1]:
        statues_size += 1
        
        if statues_size not in sorted_statues:
            output.append(statues_size)
        else: 
            continue
    return len(output)
    
print(makeArrayConsecutive2([6, 2, 3, 8])) # 3
print(makeArrayConsecutive2([0, 3])) # 2
print(makeArrayConsecutive2([5, 4, 6])) # 0 