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

balance = 100
try:
    number = int(input("Choose a number Between 0 - 32: "))
except ValueError:
    print("That wasn't a number!")
    number = -1

while number not in range(0,33):
    print("Invalid Number")
    number = int(input("Choose a number Between 0 - 32: "))
print(f"Number:{number} picked")


bet = (int(input(f"Remaining Balance:{balance}  Choose Bet Size, ")))
while bet < 1 or bet > balance:
    print("Invalid bet!")
    bet = int(input(f"Enter a bet between $1 and ${balance}: "))
print(f"Bet accepted: ${bet}")


ball_result = spin()

print(check_result(number,ball_result) + " " + str(balance))

