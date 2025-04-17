def mess2(x, y, z = 2):
    x += 1
    z = 0
    return x + y + z

x = 2
y = 1
z = 4
print(f'mess2(x, y) = {mess2(x, y)}, x = {x}, y = {y}, z = {z}')