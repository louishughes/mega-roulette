## Ask user to generate a random number between 1 and 52 
## User starts with $100
## Ask them to place a bet size
## 

import random 

def spin():
    return random.randrange(0,33)




def check_result(player_num,ball_num):
    if player_num == ball_num:
        return "Won"
    else:
        return "Lost"

number = int(input("Choose a number: "))
ball_result = spin()

print(check_result(number,ball_result))

