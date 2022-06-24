# Author:         Milan Haydel  
# ULID/Section:   C00419477 
# Lab #4 

# Part I
# Ask the user to enter the lengths of three sides of a triangle
side1,side2,side3 = eval(input("Enter 3 integers (separated by commas) for the triangle sides: "))


# Check for "valid" lengths ...
# if valid -- compute perimeter -- else print "invalid side lengths"
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Perimeter = ", side1 + side2 + side3)
else:
    print("Invalid lengths!")




# Part II
# Ask the user for a number
print()
number = eval(input("Enter one floating point number: "))


# Determine if the input number is positive, negative or zero
# Respond with your determination

if number > 0:
    print("You entered a positive number!")
elif number < 0:
    print("You entered a negative number!")
elif number == 0:
    print("You entered zero!")
    


# Part III
# Ask the user for how many years they have worked for a company
print()
years = eval(input("Enter years worked: "))


# Determine the category of their raise (see handout)
# Respond with your determination


if 0 <= years <= 3:
    print("Raise category = 3%")
elif 4 <= years <= 5:
    print("Raise category = 4%")
elif 6 <= years <= 7:
    print("Raise category = 5%")
elif years > 7:
    print("Raise category = 6%")
