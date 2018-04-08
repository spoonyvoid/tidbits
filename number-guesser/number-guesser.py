"""
You enter a lower limit and then you enter an upper limit.
The program will randomly generate a number between those two limits.
The program will allow you to guess what the number is and give you an indication
as to whether your guess is higher than the number or lower than the number.
It'll also keep track of the number of guesses you make!
Try and guess a number with as few attempts as possible!
"""

import random
import math

#I don't really have to use a dictionary but I'm going to use one anyway.
game_vals = {}

while True:
    try:
      game_vals["low_lim"] = int(input("Enter the lower limit.\n> "))
      game_vals["up_lim"] = int(input("Enter the upper limit.\n> "))
      if game_vals["up_lim"] == game_vals["low_lim"]:
          print("They can't be the same number! Try again!")
          continue
      game_vals["num_to_guess"] = random.randint(game_vals["low_lim"], game_vals["up_lim"])
    except ValueError:
      print("You've either inserted non-numeric values or your lower limit is higher than your upper limit. Please try again!")
      continue
    break

#Using the binary search formula to calculate the optimal number of attempts
def optimal_attempts(low, high):
    return math.ceil(math.log2(high - low + 1))

print(f"Now guess a number between {game_vals['low_lim']} and {game_vals['up_lim']}")

game_vals["attempts"] = 1
while True:
    guess = input("> ")
    try:
        if int(guess) < game_vals["num_to_guess"]:
            print("That's too low! Guess higher!")
        elif int(guess) > game_vals["num_to_guess"]:
            print("That's too high! Guess lower!")
        elif int(guess) == game_vals["num_to_guess"]:
            print("That's right!")
            break
        game_vals["attempts"] += 1
    except:
        print("That is not a valid number! Please try again.")
        continue

target_attempts = optimal_attempts(game_vals["low_lim"], game_vals["up_lim"])

print(f"It took you {game_vals['attempts']} attempt(s) to guess the number!")
print(f"The optimal number of attempts is {target_attempts}")
if game_vals["attempts"] <= target_attempts:
    print("Well done!")
else:
    print("Try harder next time!")
