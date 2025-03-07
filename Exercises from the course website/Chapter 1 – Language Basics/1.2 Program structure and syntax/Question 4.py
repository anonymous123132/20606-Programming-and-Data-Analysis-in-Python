##Question 4
"""
לפניכם תוכנית הקולטת שני מספרים שלמים, x ו־y.

אם לפחות אחד מהמספרים שווה ל־0, יש להדפיס "Error"
אם שני המספרים חיוביים, התוכנית תדפיס את התוצאה של מכפלת x ב־y
אם x חיובי ו־y שלילי, התוכנית תדפיס את הסכום של x ו־y
אם x שלילי ו־y חיובי, התוכנית תדפיס את תוצאת  החיסור של y מ־x
אם שני המספרים שליליים, התוכנית תדפיס את מנת החלוקה של x ב־y
התוכנית נכתבה ללא הזחות כלל. הוסיפו את ההזחות המתאימות במחברת, כך שהתוכנית תעבוד כנדרש.
כמה מהפקודות נותרו ללא שינוי בהזחה?

תשובה:5

x = float (input ("Please enter first number: "))
y = float (input ("Please enter second number: "))
if x == 0 or y == 0:
print ("Error")
if x > 0:
if y > 0:
print (x * y)
if y < 0:
print (x + y)
if x < 0:
if y > 0:
print (x - y)
if y < 0:
print (x / y)
"""

x = float (input ("Please enter first number: "))
y = float (input ("Please enter second number: "))
if x == 0 or y == 0:
    print ("Error")
if x > 0:
    if y > 0:
        print (x * y)
    if y < 0:
        print (x + y)
if x < 0:
     if y > 0:
        print (x - y)
     if y < 0:
       print (x / y)