def sum_of_Digits (n):
    if n < 10 :
        return n
    else:
        return n % 10 + sum_of_Digits(n // 10)

print(sum_of_Digits(12345))