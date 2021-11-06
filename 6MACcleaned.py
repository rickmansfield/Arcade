# def makeArrayConsecutive2(statues):
#     return (max(statues)-min(statues)+1)-len(statues)
"""warning the code below does NOT work!!!
However, It's a terrific example of how a loop takes
in an initial range and then regardless of the fact I
attempted to dynamically change the range on each 
iteration the loop adhears to the ORIGINAL range of (0,4)

"""
def makeArrayConsecutive2(statues):
    count = 0
    # statues.sort()
    sorted_statues = sorted(statues)
    dynamicRange = range(len(statues))
    dynamicLength = len(statues)-1
    for i in dynamicRange:
        # dynamicLength = len(statues)-1
        if i == dynamicLength:
            return count
        else:
            diff = (statues[i + 1]) - statues[i]
        if diff > 1:
            count += 1
            statues.append(statues[i]+1)
            statues.sort()
            dynamicRange = range(len(statues))
            dynamicLength = len(statues)-1
            # print("statues after appending:", statues)
    return count

print(makeArrayConsecutive2([6, 2, 3, 8]))
# print(makeArrayConsecutive2([0, 3]))
# print(makeArrayConsecutive2([5, 4, 6]))