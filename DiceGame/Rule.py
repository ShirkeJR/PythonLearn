from collections import Counter


class Rule(object):
    @staticmethod
    def calculate_points(rule, dices):
        most_common_result = Counter(dices).most_common()
        if rule == "a":
            return sum(dice.result == 1 for dice in dices)
        elif rule == "b":
            return sum(dice.result == 2 for dice in dices) * 2
        elif rule == "c":
            return sum(dice.result == 3 for dice in dices) * 3
        elif rule == "d":
            return sum(dice.result == 4 for dice in dices) * 4
        elif rule == "e":
            return sum(dice.result == 5 for dice in dices) * 5
        elif rule == "f":
            return sum(dice.result == 6 for dice in dices) * 6
        elif rule == "g":
            if most_common_result[0][1] == 3:
                return most_common_result[0][0].result * most_common_result[0][1]
        elif rule == "h":
            if most_common_result[0][1] == 4:
                return most_common_result[0][0].result * most_common_result[0][1]
        elif rule == "i":
            if len(most_common_result) == 2:
                return 25
        elif rule == "j":
            a = [1, 2, 3, 4]
            b = [2, 3, 4, 5]
            c = [3, 4, 5, 6]
            if a or b or c in dices:
                return 30
        elif rule == "k":
            a = [1, 2, 3, 4, 5]
            b = [2, 3, 4, 5, 6]
            if a or b in dices:
                return 40
        elif rule == "l":
            if most_common_result[0][1] == 5:
                return most_common_result[0][0] * most_common_result[0][1]
        elif rule == "m":
            return sum(dice.result for dice in dices)
        return 0

