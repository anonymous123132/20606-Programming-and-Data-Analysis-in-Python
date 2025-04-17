flag1 = False
flag2 = True

if flag1:
  if not flag2:
    print("A")
  else:
    print("B")
else:
  if not flag2:
    print("C")
  else:
    print("D")

if flag1 and not flag2:
  print ("A")
else:
  print("B")