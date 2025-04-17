num = int(input("Enter a number: "))
if num ==1 or num==2:
    num = num +1
elif num >=3 and num <=5:
    num = num -1
elif num ==6:
    num = num*2
else:
    num = num*3
print(num)