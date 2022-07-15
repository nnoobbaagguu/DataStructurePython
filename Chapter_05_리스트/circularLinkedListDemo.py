from circularLinkedList import *

list = CircularLinkedList()
list.append(30); list.insert(0, 20) # 20 -> 30
a = [4, 3, 3, 2, 1]
list.extend(a) # 20 -> 30 -> 4 -> 3 -> 3 -> 2 -> 1
list.reverse() # 1 -> 2 -> 3 -> 3 -> 4 -> 30 -> 20
list.pop(0) # 1 반환 # 2 -> 3 -> 3 -> 4 -> 30 -> 20
print("count(3):", list.count(3)) # count(3): 2
print("get(2):", list.get(2)) # get(2): 3
list.print_list()