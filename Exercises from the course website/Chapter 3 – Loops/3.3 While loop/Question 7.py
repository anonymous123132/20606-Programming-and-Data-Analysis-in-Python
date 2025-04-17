num = int(input("Please enter number:"))
if num < 100:
  print("True")
flag  = True
next_diff = num % 100 // 10 - num % 10+ 1
num = num // 10
while num >= 10:
  if num % 100 // 10 - num % 10!=next_diff:
    flag = False
    break
  else:
    next_diff += 1
    num = num // 10

print(flag)