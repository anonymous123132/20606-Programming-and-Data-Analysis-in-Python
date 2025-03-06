x = float (input ("Please enter first number: "))
y = float (input ("Please enter second number: "))
if x == 0 or y == 0:
	print ("Error")
if x > 0:
	if y > 0:
		print (x * y)
	if y < 0:
		print (x + y)
if x < 0:
	if y > 0:
		print (x - y)
	if y < 0:
		print (x / y)
