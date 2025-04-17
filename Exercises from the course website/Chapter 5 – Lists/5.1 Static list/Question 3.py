def half_list(a):
    middle = len(a) // 2
    a =a[:middle]
    return a


a= (9, 2, "hello", "11", 9)


print(half_list(a))