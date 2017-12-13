import liczby

class Test(object):
    def test_answer_type(self):
        assert isinstance(liczby.num2text(1), basestring)

    def test_zero(self):
        assert liczby.num2text(0) == 'zero'

    def test_one(self):
        assert liczby.num2text(1) == 'jeden'

    def test_two(self):
        assert liczby.num2text(2) == 'jeden'


class Liczby:
    def num2text(self, a):
        if a == 0:
            return "zero"
        elif a == 1:
            return "jeden"
        elif a == 2:
            return "dwa"