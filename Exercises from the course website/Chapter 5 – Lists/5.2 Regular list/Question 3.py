def min2_list(a):
    copy_list = a.copy()
    copy_list.sort()
    min_val = a[0]
    if copy_list[0] != copy_list[1]:
        min_val = copy_list[0]
        return min_val
    else:
        for i in range(1,len(copy_list)):
            if copy_list[i] != copy_list[0]:
                min_val = copy_list[i]
                return min_val


a =[ 3,7,-1,4,-1]
print(min2_list(a))