"""create 2 lists 2 cards games
we display each set of cards
we draw 10 cards in each set
we show each """

import random

#defining the initial parameters

set_of_cards=["1","2","3","4","5","6","7","8","9","10","V","D","R"]
set_of_colors=["spade", "heart", "diamond", "club"]

#generating the set of cards

soc_1=[]
soc_2=[]

for card in set_of_cards:
    for color in set_of_colors:
        x=[card, color]
        y=' '.join(x)
        soc_1.append(y)
        soc_2.append(y)

#displaying the cards of each set

print("1st set:")
for element in soc_1:
    print(element)

print("2nd set:")
for element in soc_2:
    print(element)

#drawing 10 elements in both set of cards
tir_1=[]
tir_2=[]
count=0

while count < 10:
    y=random.choice(soc_1)
    if y not in tir_1:
        tir_1.append(y)
        count+=1

print("\n 10 elements drawn: \n")
for element in tir_1:
    print(element)

count=0
while count < 10:
    y=random.choice(soc_2)
    if y not in tir_2:
        tir_2.append(y)
        count+=1

print("\n 10 elements drawn: \n")
for element in tir_2:
    print(element)

#checking if any element of drawn_1=drawn_2
for element1 in tir_1:
    for element2 in tir_2:
        if element1==element2:
            print(element1, " is identical in both set of cards 1 and 2.")




