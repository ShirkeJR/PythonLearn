import urllib2
from xml.dom import minidom


#class Wyjatek(Exception):
#    pass

#try:
 #3   raise Wyjatek("Wyjate#k")
#except Wyjatek as ex:
    #print ex

#print ex

#response = urllib2.urlopen("https://onet.pl/")
#html = response.read()
#print html

xml = '''<?xml vestions"1.0"?>
<master>
    <imie> Tomek </imie>
    <nazwisko> Rosh </nazwisko>
</master>'''

print xml
doc = minidom.parseString(xml)
els = doc.getElementsByTagName("master")[0]

print els