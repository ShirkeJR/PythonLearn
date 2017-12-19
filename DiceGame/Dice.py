import random


class Dice(object):
    def __init__(self):
        self.min = 1
        self.max = 6
        self.is_locked = False
        self.result = 0

    def roll(self):
        if not self.is_locked:
            self.result = random.randint(self.min, self.max)

    def lock(self):
        self.is_locked = True

    def un_lock(self):
        self.is_locked = False

    def __eq__(self, other):
        return self.result == other.result

    def __hash__(self):
        return hash(self.result)
