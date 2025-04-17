seniority = int(input("Please enter seniority (1/2): "))          # ותק
soldier = int(input("Please enter soldier status (1/2/3): "))  # חייל
format = int(input("Please enter format (1/2): "))          # מתכונתהנחיה
semester = int(input("Please enter semester (1/2): "))        # סמסטר


sum =0

if seniority ==1:
    sum =  2079
else:
    sum = 1539

if soldier == 1:
    sum = sum*0.5
elif soldier == 2:
    sum = sum*0.9

if format == 2:
    sum = sum +301

if semester == 2:
    sum = sum+286
sum = sum +59
sum = ((sum * 10 + 0.5) // 1 / 1000)
print("Tuition:",sum)