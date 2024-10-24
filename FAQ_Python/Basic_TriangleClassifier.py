a = float(input("enter length of a : "))
b = float(input("enter length of b : "))
c = float(input("enter length of c : "))
def Triangle_type(a, b, c):
    if a == b and a == c:
        return "this is equilateral triangle"
    elif a == b or a == c or b == c:
        return "this is isosceles triangle"
    else:
        return "this is scalene triangle"
result = Triangle_type(a, b, c)
print(result)