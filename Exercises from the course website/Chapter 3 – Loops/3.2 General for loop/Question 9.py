first_max = second_max = float('-inf')
for item in [12.5, 10.8, 16.9, 13.3, 11.4, 11.3, 13.7, 10.4]:
    if item > first_max:
        second_max = first_max
        first_max = item
    elif first_max > item > second_max:
        second_max = item
print(second_max)