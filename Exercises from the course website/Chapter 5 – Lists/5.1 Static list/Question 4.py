def print_list(a,b):
    res = tuple()
    for i in b:
        if len(a) > i and i>=0:
            res += (a[i],)
    return res

a = (9, 2, "hello", "11", 9, 2)
b = (2, 3, 4, -2, 8)
print(print_list(a, b))