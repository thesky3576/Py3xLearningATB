n = int(input("enter number :"))
a = 0
b = 1
print(a)
for i in range(a, n):
    c = a+b
    print(c)
    a = b
    b = c
    i += 1
