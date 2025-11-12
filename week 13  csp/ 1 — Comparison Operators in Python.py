# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a) #otput of 3
print(b) # output of 4
print(a==b) #output false

print(a == b)   # False #checks fpr equallity
print(a != b)   # True #checks if it is not equal to another vaule
print(a > b)    # False #checks if it is greater then another value
print(a < b)    # True #checks is it is less than another vaule
print(a >= b)   # False #checks for greater than ot equal to
print(a <= b)   # True #checks for lless than por equal to


#predict the output of the following comparisons:
10 > 5  #True
7 == 2 * 3 + 1 # True
8 != 8 #False 
4 <= 2 + 2 #True

# Write 3 examples that result in True and 3 that result in False.
7 > 6
8 == 4 * 2
21 >= 10

10 >= 15
10 != 10
41 == 55

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.
# The password must be at least 8 characters long 
# and contain at least one digit.password = "mypassword1"


score = int(input("What is your score?"))
#make score for all grading spectrues
# If score 90-100 it is a A
# If score between 80 - 89 it is a B
# If score between 70 -79 it is a C
# If score between 61 - 90 it is a D
# Else you failed
if score>=90:
    print("You passed the test and got an A!")
elif score<=90 & score <= 80:
    print("You passed the test with a B!")
elif score >=70 & score <=79:
    print("You got a c!")
elif score >=60 & score <= 69:
    print("You got a D!")
else:
    print("You didn't pass")

#ask for password
password = input("What is your password")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid")
else:
    print("Password is invalid." \
    "It must contain at least 8 characters long and contain at least one digit.")
