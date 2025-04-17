def max_list_up(a):
    max_list = tuple()
    max_list += (a[0],)
    MaxCheck = True
    MaxLastNum = a[0]
    for i in range(1,len(a)):
        if a[i] > a[i-1]:
            max_list+=(a[i],)
            MaxLastNum = a[i]
        elif(MaxCheck == False and a[i] > MaxLastNum):
            max_list = tuple()
            max_list += (a[i],)
        else:
            MaxCheck = False
    return max_list

a= (1, 2, 2, 3, 5, 4, 6, 7, 8, 1)
print(max_list_up(a))