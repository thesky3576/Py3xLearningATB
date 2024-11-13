numbers = [1,2,3,4,5,6,7,8,9,10]

def even_Numbers(num):
    return num % 2 == 0
def greater_than_five(num):
    return num > 5
#filters
filtered_even = list(filter(even_Numbers,numbers))
print(filtered_even)
#filters
greater_num = list(filter(greater_than_five,numbers))
print(greater_num)
