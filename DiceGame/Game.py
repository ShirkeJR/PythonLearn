import os
from Player import *
from Computer import *


class Game(object):
    def __init__(self):
        self.game_round = 1
        self.computer_points = 0
        self.player_points = 0
        self.player = Player()
        self.computer = Computer()

    def start(self):
        while True:
            option = 0
            os.system("cls")
            print "***************"
            print "**Gra w Kosci**"
            print "***************"
            print "1. Nowa gra"
            print "2. Exit"
            print "***************"
            try:
                option = input("Wybierz opcje: ")
            except (NameError, SyntaxError):
                os.system("cls")
                print "Sprobuj ponownie. [1, 2]\n"
            if option == 1:
                self.newGame()
            elif option == 2:
                exit(1)
            else:
                pass

    def newGame(self):
        print "\n*Rozpoczynamy gre*"
        print "Punkty gracz " + str(self.player_points)
        print "Punkty komputera " + str(self.computer_points)
        raw_input("(Wcisnij enter, by zaczac potyczke)")
        while self.game_round <= 13:
            os.system("cls")
            print "---Runda: " + str(self.game_round) + "--------"
            self.playerMove()
            self.computerMove()
            self.game_round += 1
            print "\nPunkty gracza: " + str(self.player_points)
            print "Punkty komputera: " + str(self.computer_points)
            print "----------------------------------------------"
        print "Wynik: ",
        if self.player_points > self.computer_points:
            print "Gracz wygrywa z " + str(self.player_points) + " punktami"
        else:
            print "Komputer wygrywa z " + str(self.computer_points) + " punktami"
        raw_input("(Wcisnij enter, by zakonczyc potyczke)\n")
        self.clearGame()

    def clearGame(self):
        self.game_round = 1
        self.computer_points = 0
        self.player_points = 0
        self.player.clear_rules()
        self.computer.clear_rules()

    def playerMove(self):
        raw_input("(Wcisnij enter, bu rzucic kostkami)")
        rolls = self.player.first_roll()
        while rolls >= 0:
            answer = 10
            self.player.show_dices()
            self.player.possible_rules()
            print "1. Zabierz kosc ze stolu"
            print "2. Zakoncz runde wyborem punktow"
            if rolls > 0:
                print "3. Rzuc ponownie  " + str(rolls) + "/3"
            try:
                answer = input("Wybor: ")
            except (SyntaxError, NameError, UnboundLocalError):
                print "Nie poprawna wartosc\n"
            if answer == 1:
                self.lockDice()
            elif answer == 3 and rolls > 0:
                rolls = self.player.roll_dices()
            elif answer == 2:
                rule = raw_input("Podaj regule: ")
                self.player_points += self.player.lock_rule(rule)
                break
        self.player.clear_round()

    def lockDice(self):
        os.system("cls")
        self.player.show_dices()
        try:
            diceToTake = input("Ktora kostke zabrac?: ")
            if diceToTake in range(0, 7):
                  if not self.player.lock_dice(diceToTake):
                    print "Nie ma takiej kostki\n"
            else:
                  print "Zly zakres\n"
        except (SyntaxError, NameError):
            print "Nie poprawne dane\n"

    def computerMove(self):
        print "Tura komputera...."
        rolls = self.computer.first_roll()
        roll = random.randint(1, 3)
        while rolls >= roll:
            self.computer.show_dices()
            rolls = self.computer.roll_dices()
        self.computer_points += self.computer.lock_rule(self.computer.best_rule())
        self.computer.clear_round()
