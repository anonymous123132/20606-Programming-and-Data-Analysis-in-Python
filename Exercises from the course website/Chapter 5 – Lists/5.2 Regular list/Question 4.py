def even_end(a):
    list_even = []
    list_odd = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            list_even.append(a[i])
        else:
            list_odd.append(a[i])
    list_odd.extend(list_even)

    return list_odd


a = [7,2,4,3,2,1]
print(even_end(a))