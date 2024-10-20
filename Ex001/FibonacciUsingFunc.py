def fibonacci(n) :
    if n<=1 :
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)
#n = int(input("enter the number to get fibonacci"))
print(fibonacci(6))