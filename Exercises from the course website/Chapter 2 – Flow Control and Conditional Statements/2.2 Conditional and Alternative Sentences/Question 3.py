name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

if name:

   print("Thank you,", name)

else:

   print("Name can’t be empty")

if age:

   print("Age is ok")

else:

   print("Age can’t be zero")

if name and age:

  print(f'Hello {name}, you will be {age + 1} next year')