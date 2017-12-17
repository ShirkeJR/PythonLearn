from random import *

class Dice(object):
    def __init__(self):
        self.min = 1
        self.max = 6
        self.isLocked = False
        self.result = 0

    def roll(self):
        if not self.isLocked:
            self.result = random.randint(self.min, self.max)

    def lock(self):
        self.locked = True

    def unLock(self):
        self.locked = False
