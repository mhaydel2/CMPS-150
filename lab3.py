# lab3.py

# Author:        Milan Haydel
# ULID/Section:  C00419477 / 150-002
 
 
# print a couple of blank lines before the program begins
# asking for input



# ask the user for the radius of the pizza (in inches)  
radius = eval(input("Enter radius of pizza: "))

# ask for the price of the pizza 
price = eval(input("Enter pizza price: "))

# compute the price of the pizza per square inch
area = 3.14159 * radius ** 2


# print the price NOT rounded
print ("Price per square inch = $", price/area)

import math

# print the price rounded to 2 decimal places
print ("Price per square inch = $", round(price/area,2),"\t(rounded)")








# print a couple of blank lines before the next section of code begins
# asking for input 
print ("\n\n")


# ask the user to enter a 3-letter word
# you are allowed only ONE input statement

word = input("Enter a 3-letter word: ")

# print the ASCII code (a number) for each letter of the word just input

print (word[0],"=",ord(word[0]))
print (word[1],"=",ord(word[1]))
print (word[2],"=",ord(word[2]))



# print a couple of blank lines when the program is done
print ("\n\n")

