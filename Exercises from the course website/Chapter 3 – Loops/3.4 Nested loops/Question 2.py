start = 2
end = 1000
for num in range (start, end+1):
    is_prime = True
    for j in range(start, num//2+1):
        if num % j == 0:
            is_prime = False
            break
    print("num:", num, "is_prime:", is_prime)
