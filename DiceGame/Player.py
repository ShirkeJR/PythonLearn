from User import *

class Player(User):
    def __init__(self):
        User.__init__(self)

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

    def show_dices(self):
        User.show_dices(self)
        print "W reku: ",
        for dice in self.dices:
            if dice.is_locked:
                print " " + str(dice.result),
        print ""
