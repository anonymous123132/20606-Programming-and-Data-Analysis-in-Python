sum = 0
count = 0
number = int(input("Please enter number:"))
while number > 0:
    sum += number
    count += 1
    number = int(input("Please enter number:"))

print("The average is", sum / count)
