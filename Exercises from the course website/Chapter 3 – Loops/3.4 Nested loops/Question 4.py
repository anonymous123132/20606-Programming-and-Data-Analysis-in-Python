name = input("Please enter name, EMPTY to exit")
while name != "EMPTY":
       sum = 0
       count = 0
       grade = int(input("please enter grade, -1 to stop"))
       while grade > 0:
              sum += grade
              count += 1
              grade = int(input("please enter grade, -1 to stop"))
       print(name,":", sum / count)
       name = input("Please enter name, EMPTY to exit")