import urllib2

response = urllib2.urlopen("https://google.pl/")
with open("google.html", "w") as f:
    f.write(response.read())