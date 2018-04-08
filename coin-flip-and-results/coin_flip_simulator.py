#Flips a coin n times and returns the amount of heads and tails obtained.
#Also returns the amounts as a percentage of n (or the number of flips).

import random

def flip_coin(n):
    i = 0
    head_count = 0
    tail_count = 0

    while i < n:
        result = random.randint(0,1) #0 is heads, 1 is tails
        if result == 0:
            print(f"Flip No. {i}: You got heads!")
            head_count += 1
        else:
            print(f"Flip No. {i}: You got tails!")
            tail_count += 1
        i += 1

    head_percent = (head_count / n) * 100
    tail_percent = (tail_count / n) * 100

    message = f"You got {head_count} head(s) and {tail_count} tail(s).\n"
    message += f"Heads accounted for {head_percent} percent of the total.\n"
    message += f"Tails accounted for {tail_percent} percent of the total."

    return message

flip_times = int(input("How many times do you want to flip a coin?\n> "))
print(flip_coin(flip_times))
