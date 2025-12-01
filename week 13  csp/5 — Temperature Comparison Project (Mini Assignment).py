# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

weather = int(input("What is the weather today?"))
if weather <= -10:
    print("Extreme weather warning")
if weather <=65:
    print("Its is cold outside today")
if weather <65 and weather >=80:
    print("Its is warm today")
if weather >80 and weather <=110:
    print("Today is really hot")
if weather  >110:
    print("extreme weather warning")
