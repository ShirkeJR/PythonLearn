import re

regex_email = re.compile(
    r'''(?P<adres>
    (?P<login>[\w+.]+)
    @
    (?P<domena>\w+(\.\w+)+)
    )''',
    re.IGNORECASE | re.VERBOSE
)

tekst = u'maill@poczta.pl, "jan.nowak@wp.pl"'

for match_object in regex_email.finditer(tekst):
    print match_object.groupdict()


