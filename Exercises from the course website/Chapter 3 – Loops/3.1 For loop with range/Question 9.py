n = int(input("Please enter n: "))
answer = 0
if n <= 2:
    answer = n - 1
else:
    a, b = 0, 1
    for item in range(2, n):
        a, b = b, a + b
    answer = b
print(answer)