Lst = [2,3,4,9,8,5,7]
#for counting specific element in the list
print(Lst.count(3))
#to sort list by ascending order
Lst.sort()
print(Lst)
# to add element in the order (it will add at the last)
Lst.append(10)
print(Lst)
# to insert element at particular index
Lst.insert(0,1)
print(Lst)
#to remove the last element in the list (if index not given)&&
# Particular index element(if index is given)
Lst.pop(3)
# to reverse the elements in the list
Lst.reverse()
print(Lst)
# to find the element at the particular index
print(Lst.index(3))
# to add entire list with another list
Lst.extend([6,7,4,1])
print(Lst)
#remove occurance of specific element from list (here 3 is element in the list)
Lst.remove(3)
# to empty the entire list
Lst.clear()