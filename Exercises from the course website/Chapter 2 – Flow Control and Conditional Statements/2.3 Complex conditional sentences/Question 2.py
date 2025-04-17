num = int(input("Enter a number: "))
if num<10:
    print(num, "small")
elif num<100:
    print(num, "medium")
elif num<1000:
    print(num, "big")
else:
    print(num, "very big")
