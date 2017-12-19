from Dice import *
from Rule import *
from constants import RULES

class User(object):
    def __init__(self):
        self.dices = []
        self.number_of_dices = 5
        self.used_rules = []
        for i in range(self.number_of_dices):
            self.dices.append(Dice())
        self.roll_round = 3

    def get_points_from_rule(self, rule):
        points_from_rule = Rule.calculate_points(rule, self.dices)
        return points_from_rule

    def lock_rule(self, rule):
        if self.not_used_rule(rule) and (rule in RULES):
            self.used_rules.append(rule)
        else:
            print "Nie wybrales reguly, wiec wybieram ja za ciebie"
            rule = self.get_first_possible_rule()
            self.used_rules.append(rule)
        return self.get_points_from_rule(rule)

    def get_first_possible_rule(self):
        for rule in RULES:
            if self.not_used_rule(rule):
                return rule

    def clear_rules(self):
        self.used_rules = []

    def not_used_rule(self, rule):
        return rule not in self.used_rules

    def first_roll(self):
        for dice in self.dices:
            dice.roll()
        return self.roll_round

    def roll_dices(self):
        if self.roll_round != 0:
            for dice in self.dices:
                dice.roll()
            self.roll_round -= 1
        return self.roll_round

    def clear_round(self):
        self.roll_round = 3
        self.un_lock_all_dices()

    def lock_dice(self, result):
        for dice in self.dices:
            if dice.result == result:
                if not dice.is_locked:
                    dice.lock()
                    return True
        return False

    def un_lock_all_dices(self):
        for dice in self.dices:
            dice.un_lock()

    def show_dices(self):
        print "\nNa stole: ",
        for dice in self.dices:
            if not dice.is_locked:
                print " " + str(dice.result),
        print ""