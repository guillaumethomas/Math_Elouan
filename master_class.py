import sys, inspect
from random import randint
from operator import add, sub, mul, truediv
from helper import xdict, freeze

class Addition:
    """Addition"""

    def __init__(self, max_value, nb_type):
        self.type = self.__class__.__name__
        self.max_value = max_value
        self.operator = " + "
        self.op = add
        self.nb_type = nb_type_dic[nb_type]()
        self.case = None

    def __str__(self):
        return "member of {}".format(self.type)

    def new_case(self):
        a = self.nb_type.val(self.max_value)
        b = self.nb_type.val(self.max_value)
        if b > a:
            a, b = b, a
        return [a, b, self.op(a, b)]

    def pr_case(self):
        lst = self.new_case()
        self.case = lst
        return str(lst[0]) + self.operator + str(lst[1]) + " = ? "



class Soustraction(Addition):
    """Soustraction"""

    def __init__(self, max_value, nb_type):
        Addition.__init__(self, max_value, nb_type)
        self.operator = " - "
        self.op = sub


class Multiplication(Addition):
    """Multplication"""

    def __init__(self, max_value):
        Addition.__init__(self, max_value)
        self.operator = " X "
        self.op = mul


class Division(Addition):
    """Division"""

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

nb_type_dic = xdict(Int=IntNumb)
nb_type_dic=freeze(nb_type_dic)



def print_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj)

if __name__ == "__main__":
    print_classes()








