# Write a Python program that takes two lists and returns True if
# they have at least one common member.

def Common_data(lst1,lst2):
    result = False
    for i in lst1:
        for j in lst2:
            if i == j:
                result = True
                return result
lst1 = [1,2,3,4,5]
lst2 = [5,4,3,6,7,8]
print(Common_data(lst1,lst2))


