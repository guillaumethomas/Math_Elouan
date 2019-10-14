from random import randint
from operator import add, sub, mul, truediv

class Addition:

    def __init__(self, max_value, nb_type):
        self.type = self.__class__.__name__
        self.max_value = max_value
        self.operator = " + "
        self.op = add
        self.nb_type = nb_type_dic[nb_type]()
    pass

    def new_case(self):
        a = self.nb_type.val(self.max_value)
        b = self.nb_type.val(self.max_value)
        if b > a:
            a, b = b, a
        return [a, b, self.op(a, b)]


class Soustraction(Addition):
    def __init__(self, max_value, nb_type):
        Addition.__init__(self, max_value, nb_type)
        self.operator = " - "
        self.op = sub


class Multiplication(Addition):
    def __init__(self, max_value):
        Addition.__init__(self, max_value)
        self.operator = " X "
        self.op = mul


class Division(Addition):
    def __init__(self, max_value):
        Addition.__init__(self, max_value)
        self.operator = " / "
        self.op = truediv


class IntNumb:
    def __init__(self):
        pass

    def val(self, max_value):
        return randint(0, max_value)

class Fraction:
    pass


class Decimal:
    pass

nb_type_dic = {
    "Int": IntNumb,
}








