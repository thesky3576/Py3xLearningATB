a= int(input("enter the number : "))

if a <= 1:
    print("given number is not prime")
elif a ==2 :
    print("given number is prime")
else:
    for i in range (2,a):
        if a % i == 0:
            print(f"{a} is not prime")
            break
    else :
        print(f"{a} is prime")
