num = int(input("Please enter number:"))
if num < 100 or num % 10 == num // 10 % 10:
    print("False")
else:
    temp = num % 100
    num = num // 100
    flag = True
    while num >= 10 and flag == True:
        if num % 100 != temp:
             flag = False
        else:
            num = num // 100
    if num > 0 and num != temp % 10:
        flag = False
    print(flag)