import sys

fileName = "plik3.txt" #sys.argv[1]
tresc = "Mickiewicz" #sys.argv[2]

if(fileName != "-"):
    file = open(fileName, "r")
    for line in file:
        if (line.__contains__(tresc)):
            print line
    file.close()
else:
    tekst = ""
    while(True):
        line = raw_input("Podaj linie: ")
        if (len(line) < 1):
            break
        tekst += "\n" + line

    for linee in tekst:
        if (linee.__contains__(tresc)):
            print linee