from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import NUMERIC

Base = declarative_base()

class Ksiazka(Base):
    __tablename__ = "KSIAZKA"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    price = Column(String)

    def __repr__(self):
        return "<Ksiazka(id='%s', title='%s', price='%s')>" % (self.id, self.title, self.price)


class Autor(Base):
    __tablename__ = "AUTOR"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return "    <Autor(id='%s', name='%s')>" % (self.id, self.name)



class Ksiazka_Autor(Base):
    __tablename__ = "KSIAZKA_AUTOR"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    price = Column(String)

    def __repr__(self):
        return "<Ksiazka(id='%s', title='%s', price='%s')>" % (self.id, self.title, self.price)


def wyswietl(session):
    for ksiazka in session.query(Ksiazka).all():
        print ksiazka
    for autor in session.query(Autor).all():
        print autor

def dodaj(session):
    titleR = raw_input("Podaj tytul: ")
    autorR = raw_input("Podaj autora: ")
    priceR = input("Podaj cene: ")
    ksiazka = Ksiazka(title=titleR, price=priceR)
    autor = Autor(name=autorR)
    session.add(ksiazka)
    session.add(autor)
    session.commit()

engine = create_engine('sqlite:///baza2.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session = Session()

while True:
    print "1. Dodaj"
    print "2. Wystwietl"
    z = input("Opcja: ")
    if z == 1:
        dodaj(Session)
    else:
        wyswietl(Session)
    pass

