import urllib2
from xml.dom import minidom


response = urllib2.urlopen("http://webmaster.helion.pl/starocie/xml/pierwszy_dokument.htm")
html = response.read()

print html

elements = minidom.parse(html)
th1 = elements.getElementsByTagName('h1')

for ele in th1
    #name = ele.getAttribute()
    #print name


