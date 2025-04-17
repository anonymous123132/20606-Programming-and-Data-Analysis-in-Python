n = 5
m = 4
for item1 in range(n):
    for item2 in range(m):
        print('*', end="")
    print()

n = 7
for item1 in range(n, 0, -1):
  for item2 in range(item1):
   print('*', end="")
  print()

n = 7
for item1 in range(n):
    for item2 in range(n - item1 - 1):
        print(' ', end='')
    for item2 in range(2 * item1 + 1):
        print('*', end='')
    print()
for item1 in range(n - 2, -1, -1):
    for item2 in range(n - item1 - 1):
        print(' ', end='')
    for item2 in range(2 * item1 + 1):
        print('*', end='')
    print()