import json

slownik = {
    'k1': 'w1',
    'k2': 2,
    3: [1, 2, 3],
}

jsonStr = json.dumps(slownik)
print jsonStr

slownik2 = json.loads(jsonStr)
print slownik2

