import urllib2
from xml.dom import minidom


response = urllib2.urlopen("http://webmaster.helion.pl/starocie/xml/pierwszy_dokument.htm").read()

print response

elements = minidom.parseString(response)
th1 = elements.getElementsByTagName("h1")

for element in elements:
        el = element.getElementsByTagName("title")
        print el


