import sys, inspect
from random import randint, uniform
from operator import add, sub, mul, truediv
from helper import xdict, freeze
from fractions import Fraction


class Operation:
    """Operation"""

    def __init__(self, max_value, nb_type, operator, op):
        self.type = self.__class__.__name__
        self.max_value = max_value
        self.operator = operator
        self.op = op
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


class Addition(Operation):
    """Addition"""

    def __init__(self, max_value, nb_type):
        Operation.__init__(self, max_value, nb_type, " + ", add)

class Soustraction(Operation):
    """Soustraction"""

    def __init__(self, max_value, nb_type):
        Operation.__init__(self, max_value, nb_type, " - ", sub)

class Multiplication(Operation):
    """Multplication"""

    def __init__(self, max_value, nb_type):
        Operation.__init__(self, max_value, nb_type, " X ", mul)

class Division(Operation):
    """Division"""

    def __init__(self, max_value, nb_type):
        Operation.__init__(self, max_value, nb_type, " / ", truediv)


class IntNumb:
    def __init__(self):
        pass

    def val(self, max_value):
        return randint(0, max_value)

class Fract:
    def __init__(self):
        pass

    def val(self, max_value):
        return Fraction(str(round(uniform(0,max_value),2)))



class Decimal:
    def __init__(self):
        pass

    def val(self, max_value):
        return round(uniform(0, max_value), 3)

nb_type_dic = xdict(Int=IntNumb, Frac=Fract, Dec=Decimal)
nb_type_dic=freeze(nb_type_dic)



def print_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj)

if __name__ == "__main__":
    print_classes()








