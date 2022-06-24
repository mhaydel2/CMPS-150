# Author: Milan Haydel
# ULID/Section: C00419477 / Section 002
myCity = input("Enter your city: ")
speed = eval(input("Enter the speed of a vehicle in mph: "))
hours = eval(input("Enter the hours a vehicle traveled: "))

# compute the distance vehicle traveled
distance = speed * hours

# print output
print()
print("Your home town is:", myCity)
print("The vehicle traveled", distance, "miles!")
