from User import *


class Computer(User):
    def __init__(self):
        User.__init__(self)

    def best_rule(self):
        computer_rules = [rule for rule in RULES if rule not in self.used_rules]
        best_points = 0
        computer_rule = None
        for rule in computer_rules:
            points = self.get_points_from_rule(rule)
            if points >= best_points:
                best_points = points
                computer_rule = rule
        return computer_rule
