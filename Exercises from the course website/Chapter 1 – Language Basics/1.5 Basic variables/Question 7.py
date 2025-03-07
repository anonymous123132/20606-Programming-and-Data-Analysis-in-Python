"""
שאלה 7
לפניכם תוכנית ההופכת מספר תלת־ספרתי.
דוגמה:
עבור המספר 123, המספר ההפוך יהיה 321. השלימו את התוכנית באמצעות גרירה.
"""
num = 123
reverse_num = num % 10
reverse_num = (reverse_num * 10 ) + (num // 10 % 10)
reverse_num = (reverse_num * 10 ) + (num // 100)
print(reverse_num)
