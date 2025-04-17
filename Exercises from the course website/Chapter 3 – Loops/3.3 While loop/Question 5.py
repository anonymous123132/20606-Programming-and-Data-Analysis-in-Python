all_even = True
num = int(input("Please enter number:"))
while num != 0 and all_even == True:
    if num % 2 != 0:
        all_even = False
    else:
        num = num // 10

print(all_even)