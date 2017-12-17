from os import system

class Game(object):
    def __init__(self):
        self.gameRound = 1
        self.computerPoints = 0
        self.userPoints = 0
        pass

    def start(self):
        while True:
            option = 0
            system("cls")
            print "***************"
            print "**Gra w Kosci**"
            print "***************"
            print "1. New game"
            print "2. Exit"
            print "***************"
            try:
                option = input("Choose option: ")
            except (NameError, SyntaxError):
                system("cls")
                print "Try again. [1, 2]\n"
            if option == 1:
                self.newGame()
            elif option == 2:
                exit(1)
            else:
                pass

    def newGame(self):
        system("cls")
        print "*Rozpoczynamy gre*"
        print "User points: " + str(self.userPoints)
        print "Computer points: " + str(self.computerPoints)
        while self.gameRound <= 13:
            print "---Runda: " + str(self.gameRound) + "--------"
            self.playerMove()
            self.computerMove()
            self.gameRound += 1
            print "Player points: " + str(self.userPoints)
            print "Computer points: " + str(self.computerPoints)
            print "----------------------------------------------"
        print "Result: ",
        if self.userPoints > self.computerPoints:
            print "User win with: " + str(self.userPoints) + " points"
        else:
            print "Computer win with: " + str(self.computerPoints) + " points"
        raw_input("(Press enter)")
        self.clearGame()

    def clearGame(self):
        self.gameRound = 1
        self.computerPoints = 0
        self.userPoints = 0

    def playerMove(self):
        pass

    def computerMove(self):
        pass