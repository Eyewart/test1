"""create a class representing a set of cards
52 cards
a card is a value and a color ()"""

import random

class Card:

    def __init__(self, color, value):
        self.color=color
        self.value=value

    def __repr__(self):
        card=self.color + " " + self.value
        return card

    def display (self):
        result=self.value + " " + self.color
        return result

class SetOfCards:

    def __init__(self):

        self.cards=[]

        values=["1","2","3","4","5","6","7","8","9","10","V","D","R"]
        colors=["Spade", "Heart", "Diamond", "Club"]

        for value in values:
            for color in colors:
                self.cards.append(Card(value, color))

    def MixGame(self):
        """use shuffle from random module for mixing the set of cards"""
        random.shuffle(self.cards)

    def DisplayGame(self):
        """display the entire game"""
        print(self.cards)

    def RandomDraw(self):
        """draw a card randomly and display his name"""
        print(len(self.cards))
        if(len(self.cards)==0):
            print("No more cards!")
            return
        else:
            d = random.randint(0, (len(self.cards)-1))
            print("Random card is: ", self.cards[d])
            card=str(self.cards[d])
            del self.cards[d]
            return card

