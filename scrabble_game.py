"""Scrabble:
a draw includes 7 lettres
it's valid if at least 2 vowels are picked
"""

import random

#defining generic parameters

list_of_letters=["15","9","6","6","6","6","6","6"]
list_of_characters=["E","A","I","N","O","R","S","T"]

bowl_of_elements=[]

#generate the bowl for the drawing
for letters in list_of_letters:
    for characters in list_of_characters:
        bowl_of_elements.append(characters)

v=0 #number of vowels picked
number_of_try=7

letters_picked=[]
list_of_vowels=["E","A","I","O"]

while v < 2:
    for i in range(0,number_of_try):
        x=random.choice(bowl_of_elements)
        letters_picked.append(x)
        if x in list_of_vowels:
            v+=1
    print(letters_picked)
    letters_picked=[]




