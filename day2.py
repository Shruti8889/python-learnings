#Day 2 - If-Else Statements

#If Statement 
number = 15
if number > 0:
    print("The number is positive.")

#If Boolean conditon
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#If-Elif Statement
Salary = 35
IncrementedSalary = 35
if IncrementedSalary > Salary:
   print("Congrats! Your salary is incremened")
elif IncrementedSalary==Salary:
   print("Its time to switch the company")

#If-Else Statement
Bonus = 5
IncrementedSalary = IncrementedSalary - Bonus
if IncrementedSalary > Salary:
   print("Congrats! Your salary is incremened")
elif IncrementedSalary==Salary:
   print("Its time to switch the company")
else:
   print("Its their loss.")

#Logical Operators - and, or, not
TotalSalary = 40
if TotalSalary > Salary and Salary > IncrementedSalary:
   print("Both conditions are true")

if TotalSalary < Salary or Salary > IncrementedSalary:
   print("Atleast one of the condition is true")

if not TotalSalary < IncrementedSalary:
   print("Total Salary is not less than Incremented salary.")

#Nested If Statement
x = 23
if x >20:
   print("The number is above 20")
   if x > 25:
      print("The number is above 25")
   else:
    print("But the number is not above 25")  

#Practices
username = "Timmy"
password = "Test@123"
is_verified = False

if username and password and len(password)>=8 and is_verified:
   print("Login successful.")
else:
   print("Login failed.")