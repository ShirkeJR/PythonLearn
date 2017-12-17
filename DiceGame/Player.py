from Dice import *

class Player(object):
    def __init__(self):
        self.dices = []
        self.numberOfDices = 5
        for i in range(self.numberOfDices):
            self.dices.append(Dice())
        self.rollRound = 3

    def throwDices(self):
        for dice in self.dices:
            dice.roll()
        self.rollRound -= 1
