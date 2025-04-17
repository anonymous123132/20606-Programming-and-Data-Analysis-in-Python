g1 = int(input("Please enter first number: "))
g2 = int(input("Please enter second number: "))
g3 = int(input("Please enter third number: "))
g4 = int(input("Please enter fourth number: "))

g1_ok = g1 >= 0 and g1 <= 255
g2_ok = g2 >= 0 and g2 <= 255
g3_ok = g3 >= 0 and g3 <= 255
g4_ok = g4 >= 0 and g4 <= 255

if g1_ok and g2_ok and g3_ok and g4_ok:
  print("Ok")
else:
  if not g1_ok:
    print("Group 1,", g1)
  if not g2_ok:
    print("Group 2,", g2)
  if not g3_ok:
    print("Group 3,", g3)
  if not g4_ok:
    print("Group 4,", g4)