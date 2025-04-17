numbers = int(input("Enter number"))
Bigbumber  = 0

while numbers > 0:
    if Bigbumber <numbers% 10:
        Bigbumber = numbers% 10
    numbers = numbers//10
print(Bigbumber)