# Z-Casino
# number to pick from 0 to 49
# roulette compound of 50 numbers : even number = red, odd-number = black
# two possible cases:
# 1) if choosen_num=picked_num then money_back=bet*3
# 2) if the color is the same he got back 50% of his bet
# else the user lost his bet

#import the right modules

import os
from random import randrange
from math import ceil

#introduction to the game

print("Welcome to the Z-Casino!")

#declaration of the variables
current_value=1000
y=0
i=0

#declaration of the random function
def rand_num():
    return randrange(1,51)

while current_value>0:

    print("Your current wallet is ", current_value)

    while i != 1:
        choosen_num = int(input("Which number will you pick?"))
        if choosen_num > 0 and choosen_num < 51:
            i = 1
        else:
            print("Please enter a number between 1-50")

    while y != 1:
        bet=int(input("How much will you bet?"))
        if bet <= current_value and bet > 0:
            y = 1
        else:
            print("Please enter a number between 1-1000")

    #draw of the hazardous number
    y=0
    i=0
    picked_num=rand_num()
    print("The picked number is ", picked_num)

    #verification if win or lost
    if choosen_num==picked_num:
        current_value+=bet*3
    elif choosen_num%2==0 and picked_num%2==0:
        current_value+=ceil(bet*0.5)
    elif choosen_num%2!=0 and picked_num%2!=0:
        current_value+=ceil(bet*0.5)
    else:
        current_value=(current_value-bet)

print("You have lost all your money..")




