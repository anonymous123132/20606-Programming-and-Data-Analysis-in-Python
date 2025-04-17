def sumDigits(num):
    sum = 0
    while num:
        digit = num % 10
        sum += digit
        num = num // 10
        return sum
print ("Sum for 352 is: ", sumDigits(352))
