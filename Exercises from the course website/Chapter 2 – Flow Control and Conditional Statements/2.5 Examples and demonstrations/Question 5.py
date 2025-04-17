s1 = input("enter")
check = False
if len(s1) != 6:
    print("False")
elif s1[0] == s1[5] and s1[1] == s1[4] and s1[2] == s1[3]:
    print("True")
else:
    print("False")


print(check)

print( s1[0] == s1[5] and s1[1] == s1[4] and s1[2] == s1[3] and len(s1) == 6)

"""
    
    for i in range(len(s1)):
        if s1[i] == s1[-(i+1)]:
            check = True
        else:
            check = False
            break
"""