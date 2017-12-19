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

    def possible_rules(self):
        print ""
        possibleRules = [rule for rule in RULES if rule not in self.used_rules]
        i = 0
        for rule in possibleRules:
            if i == 6 or i == 9:
                print ""
            print "[" + str(rule) + "]." + RULES.get(rule) + "(" + str(self.get_points_from_rule(rule)) + ")",
            i += 1
        print "\n"

    def get_points_from_rule(self, rule):
        points_from_rule = Rule.calculate_points(rule, self.dices)
        return points_from_rule

    def lock_rule(self, rule):
        if self.not_used_rule(rule) and (rule in RULES):
            self.used_rules.append(rule)
        else:
            print "Nie wybrales reguly, wiec wybieram ja za ciebie"
            rule = self.best_rule()
            self.used_rules.append(rule)
        return self.get_points_from_rule(rule)

    def best_rule(self):
        rules = [rule for rule in RULES if rule not in self.used_rules]
        best_points = 0
        best_rule = None
        for rule in rules:
            points = self.get_points_from_rule(rule)
            if points >= best_points:
                best_points = points
                best_rule = rule
        return best_rule

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
        print "W reku: ",
        for dice in self.dices:
            if dice.is_locked:
                print " " + str(dice.result),
        print ""
