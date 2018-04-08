#Allows you to roll a dice as many times as you like while keeping track
#of what you've rolled and providing some basic statistics.

import random

roll_results = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
def single_roll():
    result = random.randint(1,6)
    roll_results[str(result)] += 1

    message = f"You just rolled a {result}\n\n"
    message += f"So far you've rolled the following:\n"
    message += f"{roll_results['1']} ones, {roll_results['2']} twos,\n"
    message += f"{roll_results['3']} threes, {roll_results['4']} fours,\n"
    message += f"{roll_results['5']} fives, {roll_results['6']} sixes.\n"

    return message

while True:
    go_on = input("Shall we roll the dice? [Y/N]\n> ")
    if go_on.upper() == 'Y':
        print(single_roll())
    elif go_on.upper() == 'N':
        break
    else:
        print("Only type in [Y] or [N]. Try again!")
        continue

print("All Done!")