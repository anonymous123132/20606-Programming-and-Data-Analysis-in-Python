age = int(input("Please enter your age: "))
salary = float(input("Please enter your salary: "))

if age >= 18 and age < 67:
  salary = salary - 100; # salary-=100
else:
  salary = salary + 200; # salary+=200

print(salary)