class WlasnaLista():
    def __init__(self):
        self.myList = []

    def addList(self, x):
        self.myList.append(x)

    def removeFromList(self, x):
        self.myList.remove(x)

    def sortList(self):
        self.myList.sort()

    def __add__(self, other):
        for x in other.mylist:
            self.myList.append(x)

    def getItem(self, x):
        return self.myList.__getitem__(x)


lista = WlasnaLista()

lista.addList(1)
lista.addList(2)
lista.addList(3)

print lista.myList