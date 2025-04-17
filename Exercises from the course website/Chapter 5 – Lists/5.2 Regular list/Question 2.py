def min_list(a):
    min_val = a[0]
    for i in range(1,len(a)):
        if a[i] < min_val:
            min_val = a[i]
    return min_val

a = [2,2,-1,4]
print(min_list(a))