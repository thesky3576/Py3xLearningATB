lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]
print("Given lists are"+str(lst1)+" and "+str(lst2))
# check for identical
lst1.sort()
lst2.sort()
if(lst1 == lst2):
    print("Lists are identical")
else:
    print("Lists are not identical")
