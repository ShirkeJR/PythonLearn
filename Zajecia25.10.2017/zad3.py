class Samochod(object):
    __marka = None
    __pojemnoscBaku = None
    __predkoscMaksymalna = None
    __zuzyciePaliwa = None
    def __init__(self, marka, pojemnoscBaku, predkoscMaksymalna, zuzyciePaliwa):
        self.__marka = marka
        self.__pojemnoscBaku = pojemnoscBaku
        self.__predkoscMaksymalna = predkoscMaksymalna
        self.__zuzyciePaliwa = zuzyciePaliwa
    def jedz(self, predkosc, odleglosc):
        pass

class Kabriolet(Samochod):
    __otwartyDach = None
    def __init__(self, marka, pojemnoscBaku, predkoscMaksymalna, zuzyciePaliwa, otwartyDach):
        super(Kabriolet, self).__init__(marka, pojemnoscBaku, predkoscMaksymalna, zuzyciePaliwa)
        self.__otwartyDach = otwartyDach
    def zamknijDach(self):
        self.__otwartyDach = False
    def otworzDach(self):
        self.__otwartyDach = True
    def jedz(self, predkosc, odleglosc):
        paliwo = self.jedz(predkosc, odleglosc)
        return paliwo + 0.15*paliwo

s1 = Samochod("Fiat", 15, 100, 2)
k1 = Kabriolet("Mercedes", 20, 200, 4, False)
