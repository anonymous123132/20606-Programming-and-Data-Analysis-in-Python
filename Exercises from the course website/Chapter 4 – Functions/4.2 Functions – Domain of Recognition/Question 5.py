import math
def mess5(x):
    global y
    x = 1
    y = 10
    z = 3
    return x + y + z

x = -1
y = 2
z = math.sqrt(16)
print(f'mess5() = {mess5(x)}, x = {x}, y = {y}, z = {z}')