def makeArrayConsecutive2(statues):
    return (max(statues)-min(statues)+1)-len(statues)

# def makeArrayConsecutive2(statues):
#     count = 0
#     statues.sort()
#     for i in range(len(statues)):
#         if statues[i+1]> len(statues)+1:
#             continue
#         diff = (statues[i + 1]) - statues[i]
#         if diff > 1:
#             count += 1
#             statues.append(statues[i]+1)
#             statues.sort()
#             # print("statues after appending:", statues)
#     return count

print(makeArrayConsecutive2([6, 2, 3, 8]))
print(makeArrayConsecutive2([0, 3]))
print(makeArrayConsecutive2([5, 4, 6]))