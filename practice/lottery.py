import random

# generate a lottery
lottery = random.randint (0,99)

# prompt user to enter a guess
guess =  eval(input("Enter your lottery pick (0 - 99): "))

# Get digits from lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

# get digits from guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)


if guess == lottery:
    print("Exact match! You win $10,000!")
elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
    print("You matched all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1
      or guessDigit1 == lotteryDigit2
      or guessDigit2 == lotteryDigit1
      or guessDigit2 == lotteryDigit2):
    print("You matched one digit! You win $1,000!")
else:
    print("Sorry, no match")

