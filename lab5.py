# Author:         Milan Haydel
# ULID/Section:   C00419477 / CMPS 150-002
# Lab #5

# Part I
# ask the user to enter the x coordinate (it can be a float)
x = eval(input("Enter the x coordinate: "))

# ask the user to enter the y coordinate (it can be a float)
y = eval(input("Enter the y coordinate: "))

# check for the origin, x-axis OR y-axis, then all 4 quadrants
if x > 0 and y > 0:
    quadrant = "I"
    print("\nThis point is in Quadrant ", quadrant)
elif x < 0 and y > 0:
    quadrant = "II"
    print("\nThis point is in Quadrant ", quadrant)
elif x < 0 and y < 0:
    quadrant = "III"
    print("\nThis point is in Quadrant ", quadrant)
elif x > 0 and y < 0:
    quadrant = "IV"
    print("\nThis point is in Quadrant ", quadrant)
elif x == 0 and y == 0:
    print("\nThis point is the origin")
else:
    print("\nThis point is on an axis")




# Part II
# print a blank line
print()

# pounds/kilograms table

print(" Pounds     Kilograms")
print("---------------------")

pounds = 5
kilograms = pounds * .453592
while pounds <= 50:
    print(format(pounds, '5d'),"     ", format(kilograms, '7.2f'))
    pounds = pounds + 5
    kilograms = pounds * .453592
