# Day 4 - Functions - a block of code which only runs when it is called. This avoids code repetition.

# Creating a function - defined by 'def' followed by a name and ():
def my_first_function():
    print("Hello from a function!")

my_first_function()
my_first_function()
my_first_function()

# Example of Fahrenheit to celsius without function
temp1 = 77
celsius1 = (temp1 - 32)*5/9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32)*5/9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32)*5/9
print(celsius3)

# Example of Fahrenheit to celsius with a function
def f_to_c(fahrenheit):
    return (fahrenheit - 32)*5/9

print(f_to_c(temp1))
print(f_to_c(temp2))
print(f_to_c(temp3))