first, second, third = float('inf'), float('inf'), float('inf')
for time  in [12.5, 10.8, 16.9, 13.3, 11.4, 11.3, 13.7, 10.4]:
    if time < first:
        third = second
        second = first
        first = time
    elif time<second:
        third = second
        second = time
    elif time<third:
        third = time
print(first, second, third)