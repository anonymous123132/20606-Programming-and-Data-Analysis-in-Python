def mess4():
  global y
  global z
  x = 1
  y = 3
  z = 0
  return x + y + z

x = 2
y = 1
z = 4
print(f'mess4() = {mess4()}, x = {x}, y = {y}, z = {z}')