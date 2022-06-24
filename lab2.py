# Author:       Milan Haydel
# ULID/Section: C00419477 CMPS 150-002 

# Print 2 blank lines
print()
print()

# Part I of this lab is simply using input statements and
# arithmetic expressions 
# Ask the user to input hours and hourly rate, then compute gross pay
# First, complete the following input statements 
hours = eval(input("Enter hours: "))
rate = eval(input("Enter rate: "))

# Write an equation to compute gross pay using the variables above 
grossPay = hours * rate

# Print 1 blank line
print()

# Print out hours, rate and gross pay that you just computed 
print("Hours =", hours)
print("Rate =", rate)
print("Gross Pay =", grossPay)


# ------------------------------------------------------------------
# Part II of this lab will use the math library, which means it must
# be imported
# ------------------------------------------------------------------

import math

# Print sin/cos/tan for the "common" angles of 30, 45 & 90 degrees
# Remember, sometimes one of these trig functions is undefined 
print()
print("Angle        Sine      Cosine     Tangent")
print("-------------------------------------------") 

# there are NO errors in these statements
# this converts an angle in degrees to its equivalent in radians
degree1 = 30
radian1 = math.pi / 180 * degree1
degree2 = 45
radian2 = math.pi / 180 * degree2
degree3 = 90
radian3 = math.pi / 180 * degree3

# there are NO errors in the following PRETTY print statements

print(format(degree1,"6d"),format(math.sin(radian1),"10.3f"),
      format(math.cos(radian1),"10.3f"),format(math.tan(radian1),"10.3f"))
print(format(degree2,"6d"),format(math.sin(radian2),"10.3f"),
      format(math.cos(radian2),"10.3f"),format(math.tan(radian2),"10.3f"))
print(format(degree3,"6d"),format(math.sin(radian3),"10.3f"),
      format(math.cos(radian3),"10.3f"),format(math.tan(radian3),"10.3f"))
      
