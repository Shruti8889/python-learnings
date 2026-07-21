# Day 3 - while and for loops

#while loop can execute a set of statements as long as the condition is true
i = 1
while i < 6:
    print("i:", i)
    i += 1 # This adds 1 to the existing value of i, so i = 2 now. It keeps on adding until the condition of less than 6 is fulfilled.

#break statement in while loop - stop the loop even when the condition is true
j = 1
while j < 6:
    print("j:", j)
    if j ==3:
        break
    j += 1

#continue statement in while loop - stop the current iteration and continue with the next
k = 0
while k < 5:
    k += 1
    if k == 3:
        continue
    print("k:", k)

#else statement in while loop
l = 1
while l < 6:
    print("l:", l)
    l += 1
else:
    print("l is no longer less than 6")


# For Loops - used for iterating over a sequence 

fruits = ["apple", "mango", "cherry"]
for x in fruits:
    print(x)

# Looping through a string - even strings are a sequence of characters
for x in "cherry":
    print(x)

# the break statement in the for loop
for x in fruits:
    print(x)
    if x == "mango":
        break

# the continue statement in the for loop
for x in fruits:
    if x == "apple":
        continue
    print(x)

# the range function
for x in range(6):
    print(x)

for x in range(2,9):
    print(x)

# number increment in the range and the else statement in the for loop
for x in range(2, 10, 2):
    print(x)
else:
    print("Finally Finished.")

# Nested for loop
adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x,y)