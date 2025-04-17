num = int(input("Please enter number: "))
min = max = num
while num != 0:
    if num > max:
        max = num
    if num < min:
        min = num
    num = int(input("Please enter number: "))
print("max:", max, "min:", min)