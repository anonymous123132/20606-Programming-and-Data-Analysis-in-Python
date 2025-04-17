my_list = [5,11,7,2,3,4,10]
new_list = [ n ** 2  for n in my_list  if n % 2 == 0 ]

my_list =  ['cat', 'a', 'elephant', 'hi', 'sun']
new_list  = [ word  for word in my_list  if len(word) >= 3  ]

my_list =  [30, 20, 10, 40, 50]
avg = sum (my_list) / len (my_list)
new_list = [n for n  in my_list  if n > avg  ]

st = 'Hello World'
new_list = [ char  for char  in st  if char.islower()  ]

my_list = [7, 2, 5, 1, 8, 9, 10]
new_list = [ n * 2  if n % 2 == 0  else  n  + 1 for n in my_list]