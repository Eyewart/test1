"""a game with cards
a list with:
1 -> 10
V,D,R
another with:
spades, hearts, diamonds and clubs
"""

set_of_card=["1","2","3","4","5","6","7","8","9","10","V","D","R"]
set_of_colors=["spade", "heart", "diamond", "club"]

def display_game():
    for card in set_of_card:
        print(card)

def display_game_w_colors():
    for card in set_of_card:
        for color in set_of_colors:
            print (card, "of", color)

display_game_w_colors()

