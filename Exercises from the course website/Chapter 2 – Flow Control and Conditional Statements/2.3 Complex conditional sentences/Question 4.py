first = input("Please enter first string: ")
second = input("Please enter second string: ")
if not first or not second:
  print("Error")
else:
  print(first in second and second in first)