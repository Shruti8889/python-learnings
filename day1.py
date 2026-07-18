#Day 1 - Python Basics

# 1. PRINT
print("Hello, I am Shruti.")

# 2. VARIABLES
username = "test@email.com"
password = "Test@12"
is_valid = True
age = "24"
print("Username:", username)
print("Password:", password)
print("Is Valid:", is_valid)
print("Age:", age)

# 3. MATH
Salary = 10
Bonus = 5
print("Total Salary This Month:", Salary + Bonus)
print("Password Length", len(password))

# 4. PRACTICE TASK 1: Print the above variables one line 
print(f"User: {username} | Pass: {password} | Valid: {is_valid}")

# 5. PRACTICE TASK 2: Password check - If password length is < 8 then print "Test Failed: Password too short." Else print "Test Passed".
if len(password)<8:
    print("Test Failed: Password too short.")
else:
    print ("Test Passed.")


# 6. PRACTICE TASK 3: Bug Test - If age = "24", then print(age + 5) - Observe the error
print(age + 5)