def equal_parts(a):
    sum_all = 0
    sum_part = 0
    for i in a:
        sum_all += i
    for i in range(len(a)):
        sum_part += a[i]
        if sum_part == sum_all - sum_part:
            return True
    return False


a = (1,2,3,5,1)
print(equal_parts(a))