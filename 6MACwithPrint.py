"""
have statues to arrange
constraints = 
1 ≤ statues.length ≤ 10, i.e. number of statues is between 1 & 10
0 ≤ statues[i] ≤ 20. i.e. statues are height 0 to 20 (no units given)

initialize a counter
give any list sort them in order
loop over the sorted list use len(list) for range
subtract the curent from the next if that number is >1  counter += 1
return final count
"""
def makeArrayConsecutive2(statues):
    count = 0
    statues.sort()
    print("sorted up front", statues)
    for i in range(len(statues)+1):
        if statues[i+1]> len(statues)+1:
            pass
        print("current idex:", i)
        print("Values of statues[i +1]:", statues[i+1])
        print("statues[i]:", statues[i])
        diff = (statues[i + 1]) - statues[i]
        print("diff", diff)
        if diff > 1:
            count += 1
            statues.append(statues[i]+1)
            statues.sort()
            print("statues after appending:", statues)
    return count
# def makeArrayConsecutive2(statues):
#     return (max(statues)-min(statues)+1)-len(statues)
print(makeArrayConsecutive2([6, 2, 3, 8]))
# print(makeArrayConsecutive2([0, 3]))
# print(makeArrayConsecutive2([5, 4, 6]))