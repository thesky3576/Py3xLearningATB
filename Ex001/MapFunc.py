
#map(function_name,iterables{list,tuple})
def square_no(x):
    return x ** 2
number = [1, 2, 3, 4, 5]
squared_numbers = map(square_no,number)
result = list(squared_numbers)
print(result)