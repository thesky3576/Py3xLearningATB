a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
max_num = a if (a>b and a>c) else b if (b>a and b>c) else c
print(f"the maximum number from {a},{b},{c} is {max_num}")

