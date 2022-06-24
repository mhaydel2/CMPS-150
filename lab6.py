# Author:         Milan Haydel 
# ULID/Section:   C00419477 / Section 2 
# Lab #6




# Task #1:  Print inches/centimeters table

print("Inches     Centimeters")
print("----------------------")

inches = 3

while inches <= 18:

    centimeters = inches * 2.54
    print(" ",format(inches,'2d'),"\t     ",format(centimeters,'5.2f'))

    inches = inches + 3

print()

# Task #2:  Odd and Even Numbers

# get first input item

inp = eval(input("Enter an integer (non-positive to exit): "))

import math

# repeat loop based on input item NOT being the sentinel value
while inp > 0:
    if inp % 2 == 0:
        print(inp, "is even")
    else:
        print(inp, "is odd")

    # process data - determine if input data is odd or even
    

    # get next input item
    inp = eval(input("Enter an integer (non-positive to exit): "))
