import random
number1 = random.randint(0,9)
number2 = random.randint(0,9)
print("Number1 =", number1)
print("Number2 =", number2)

if number1 < number2:
    number1, number2 = number2, number1 #simultanerous assignment

if number1 - number2 == 2:
    print("You are correct!")
else: print("Your answer is wrong.\n", number1, "-", number2, "is", number1 - number2)