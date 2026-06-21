#video link: https://youtu.be/078tYSD7K8E?si=dbDPksMeGIndv8bC


# set = {1,2,2,2,2,3,4,"Hello"}
# print(set)


collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.remove(2)
# collection.clear()
#print(collection)

set1 = {1,2,3}
set2 = (3,4,5)
# print(set1.union(set2)) #1,2,3,4,5
print(set1.intersection(set2)) #3
print(set1.difference(set2)) #1,2
print(set1.symmetric_difference(set2)) #1,2,4,5