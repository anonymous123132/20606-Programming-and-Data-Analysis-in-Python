word1 = input("Enter a word: ")
check = False
for word in word1:
    if word == "a":
        check = True
        break
if check:
    print("Yes")
else:
    print("No")