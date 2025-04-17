check = True
last = 0
for item in [2,3,6,8,9]:
    if item < last:
        check = False
        break
    else:
        last = item
print(check)