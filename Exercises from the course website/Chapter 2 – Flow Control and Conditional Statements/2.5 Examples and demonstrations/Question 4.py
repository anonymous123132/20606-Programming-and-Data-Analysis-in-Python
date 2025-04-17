s1 = input("Please enter a number: ")
s2 = input("Please enter a number: ")
s3 = input("Please enter a number: ")
s4 = input("Please enter a number: ")

counter =0

if s1[1:] == s2:
    counter +=2
    if s2[1:] == s3:
        counter +=1
        if s3[1:] == s4:
            counter +=1
print("The count of hot numbers is:", counter)