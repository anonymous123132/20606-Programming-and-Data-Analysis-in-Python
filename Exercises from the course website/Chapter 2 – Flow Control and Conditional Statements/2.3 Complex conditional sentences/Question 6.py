num2 = int(input("Please enter second number: "))
op = input("Please enter operator: ")

if op == '+':
  print(num1 + num2)
elif op == '-':
  print(num1 - num2)
elif op == '*':
  print(num1 * num2)
elif op == '/' and num2 != 0:
  print(num1 / num2)
else:
  print("Error")