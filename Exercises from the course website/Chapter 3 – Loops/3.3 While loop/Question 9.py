numbers = int(input("Enter a number: "))
Bigbumber = -1
Check = True
while numbers > 0:
    if Bigbumber <=numbers% 10:
        Bigbumber = numbers% 10
        numbers = numbers//10
    else:
        Check = False
        break
print(Check)