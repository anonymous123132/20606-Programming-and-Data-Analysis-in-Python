def int_list(list):
    final_list = []
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if (list[i] + list[j]) % 1 == 0 :
                final_list.append([list[i], list[j]])

    return final_list

print(int_list([0.4, 0.3, 0.77, 0.7, 3.4, -2.0, 7.11, 1.0]))