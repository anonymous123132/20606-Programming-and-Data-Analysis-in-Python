s1 = int(input("Enter the first number: "))
s2 = int(input("Enter the second number: "))
s3 = int(input("Enter the third number: "))
s4 = int(input("Enter the fourth number: "))

if s1 == s2 and s1 == s3 and s1 == s4:
    print("Square")
elif (s1 == s2 and s3 == s4) or (s1 == s3 and s2 == s4) or (s1 == s4 and s2 == s3):
    print("Rectangle")
else:
    print("None")