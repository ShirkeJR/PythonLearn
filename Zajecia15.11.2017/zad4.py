import re

def checkPesel(pesel):
    if re.match('[0-9]{11}$', pesel):
        print 'Pesel poprawny'
    else:
        print 'Pesel niepoprawny'


checkPesel('95091313292')