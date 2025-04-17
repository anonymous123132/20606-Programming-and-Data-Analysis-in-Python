first = 25
second = 24
if not first < second:
   print("first and second are different")

x = 3
y = 1
z = 2
if x < 1 or not z > y:
   print("x and z are different")
x = 10
y = 5
z = 10
if y >= z or z > y and z >= x:
   print("y and z are different")
x = 10
y = 5
z = 10
if y >= z and z > y or z >= x:
    print("y and z are different")
x = 10
y = 5
z = 10
if y >= z and (z > y or z >= x):
   print("y and z are different")


x = 10
y = 5
z = 10
if not y >= z and not z > y or z >= x:
   print("y and z are different")

x = 14
y = 5
z = 23
if y % 10 != 0 and x % 2 == 0 and z % 2 != 0:
    print("y and z are different")

num = 2578
if (num % 10 % 2 != 0 and (num // 10 ** 3) % 2 != 0) or  (num // 10 % 10 % 2 == 0 or  (num // 10 ** 2) % 10 % 2 == 0) :
   print("num and z are different")