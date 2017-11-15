import re

def sprawdz(pesell):
    if (re.match('[0-9]{11}$', pesell)):
        print "OK"
    else:
        print "NIE"

pesel = "9506271343"

sprawdz(pesel)

#dokończyć