max_name = name = input("Please enter name, EMPTY to exit")
max = 0
while name != "EMPTY":
    sum = 0
    count = 0
    grade = int(input("please enter grade, -1 to stop"))
    while grade > 0:
        sum += grade
        count += 1
        grade = int(input("please enter grade, -1 to stop"))
    if sum / count > max:
        max = sum / count
        max_name = name
    print(name,":", sum / count)
    name = input("Please enter name, EMPTY to exit")
print(max_name, "has the highest average:", max)