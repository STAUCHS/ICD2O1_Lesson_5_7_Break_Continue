#-------------------------------------------------------------------------
# Name:		    Lesson 5.7 Break & Continue
# Purpose:		Guessing Game with Break
# Author:		  
# Created:		06/05/2024
#-------------------------------------------------------------------------

import random

num = random.randrange(1, 101)
guess = int(input("Enter a guess: "))

while guess != num:
  if guess > num:
    print("Guess is too high. Guess again.")
  else:
    print("Guess is too low. Guess again.")

  guess = int(input("Enter a guess: "))

print("Congratulations! You guessed correct!")