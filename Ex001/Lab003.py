num = int (input("give number:"))
temp = num
reverse = 0
while temp>0:
    rem= temp % 10
    reverse = (reverse * 10) + rem
    temp = temp//10
if num==reverse:
    print("number is palindrome")
else:
    print("number is not palindrome")