max_st = st = input("Please enter string: ")
max_len = len(st)
while len(st) != 0:
    if len(st) > max_len:
        max_len = len(st)
        max_st = st
    st = input("Please enter string: ")
print(max_st, max_len)