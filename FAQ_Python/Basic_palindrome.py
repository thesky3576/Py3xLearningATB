num = int(input("enter the number to check for palindrome:"))
temp = num
reverse = 0
while temp > 0:
    rem = temp % 10
    reverse = (reverse * 10) + rem
    temp = temp // 10
if num == reverse:
    print("the given number is palindrome")
else:
    print("the given number is not palindrome")