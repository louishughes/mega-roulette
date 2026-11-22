## Ask user to generate a random number between 1 and 52 
## User starts with $100
## Ask them to place a bet size
## 

import random 
numbers_on_wheel = 10

def spin():
    return random.randrange(0,numbers_on_wheel)




def check_result(player_num,ball_num):
    global bet

    if player_num == ball_num:
        winnings = bet * (numbers_on_wheel - 1)
        add_balance(winnings)
        return "Won"
    else:
        remove_balance(bet)
        return "Lost"

def add_balance(bet):
    global balance
    balance += bet

def remove_balance(bet):
    global balance 
    balance -= bet
    if balance <= 0:
        return "Bust! Game Over"

def play():
    ##Spins the Ball on the wheel
    ball_result = spin()
    ##Prints the return value- After checking the result of the players chosen number and the result of the ball spin.
    print(check_result(number,ball_result) + " " + str(balance))



balance = 100

## Choose Starting Number
## If it isn't a number, ask again
try:
    number = int(input(f"Choose a number Between 0 - {numbers_on_wheel - 1}: "))
    ## IF it isnt a 
except ValueError:
    print("That wasn't a number!")
    number = -1
##If number is not in the range, ask again
while number not in range(0,numbers_on_wheel):
    print("Invalid Number")
    number = int(input(f"Choose a number Between 0 - {numbers_on_wheel - 1}: "))

 ## Successfully picked a number   
print(f"Number:{number} picked")

##Aask user to place a bet size
bet = (int(input(f"Remaining Balance:{balance}  Choose Bet Size, ")))

## If the bet is less than 1 or greater than the balance, ask again
while bet < 1 or bet > balance:
    print("Invalid bet!")
    bet = int(input(f"Enter a bet between $1 and ${balance}: "))
## Prints if a valid bet is placed
print(f"Bet accepted: ${bet}")

## Plays the Game
play()
