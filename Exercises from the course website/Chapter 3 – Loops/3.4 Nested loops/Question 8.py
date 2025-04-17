s = input("Please enter string: ")
n = len(s)
for len in range(1,n + 1):
    for i in range(n - len + 1):
        j = i + len - 1
        for k in range(i,j + 1):
            print(s[k],end="")
        print()