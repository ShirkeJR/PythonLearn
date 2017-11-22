import re

class Mail:
    def __init__(self, tekst):
        self.emailValidate(tekst)

    def emailValidate(self, tekst):
        if (self.regex_email.match(tekst)):
            self.email = tekst
        else:
            raise Wyjatek("Zly email")

    regex_email = re.compile(
        r'''(?P<adres>
        (?P<login>[\w+.]+)
        @
        (?P<domena>\w+(\.\w+)+)
        )''',
        re.IGNORECASE | re.VERBOSE
    )

class Wyjatek(Exception):
    pass


try:
    nowy = Mail("janusz@outlook.com")
except Wyjatek as ex:
    print "Error: " + str(ex)

