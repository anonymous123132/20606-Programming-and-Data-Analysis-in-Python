
x = 5
y = 10
z = 20

if x == y or y == z:
  print("A")
elif x != y and z > y:
  if z > 10:
    print("B")
  else:
    print("C")
elif y > z and y > x:
  print("D")
else:
  print("E")