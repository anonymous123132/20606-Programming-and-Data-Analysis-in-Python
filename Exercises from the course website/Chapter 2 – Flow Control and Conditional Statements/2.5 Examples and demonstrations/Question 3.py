tempeture1 = int(input("Enter the temperature: "))
tempeture2 = int(input("Enter the temperature: "))
tempeture3 = int(input("Enter the temperature: "))
tempeture4 = int(input("Enter the temperature: "))
count_cold= 0
count_hot = 0

if tempeture1>=30:
    count_hot = count_hot +1
elif tempeture1<=5:
    count_cold = count_cold +1

if tempeture2>=30:
    count_hot = count_hot +1
elif tempeture2 <= 5:
    count_cold = count_cold +1

if tempeture3>=30:
    count_hot = count_hot +1
elif tempeture3 <= 5:
    count_cold = count_cold +1

if tempeture4>=30:
    count_hot = count_hot +1
elif tempeture4 <= 5:
    count_cold = count_cold +1


if count_hot ==2 or count_hot ==2 or count_cold ==1:
   print("Usual")
elif count_hot ==3 or count_hot ==4 or count_cold ==2 or count_cold ==4 or count_cold ==3:
    print("Extreme")
else:
    print("Other")