import re

def extract_ips(data):
    return re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", data)


tekst = '''
192.168.0.1
adam ma konto na allegro
ant.ma.bar.ko
999.999.99.999'''

ips = extract_ips(tekst)

print ips

#dokończyć
