from sys import modules
from inspect import isclass, getmembers
from random import randint, uniform
from operator import add, sub, mul, truediv
from helper import xdict, freeze
from fractions import Fraction


class Operation:
    """Operation"""

    def __init__(self, max_value, nb_type, operator, op, size_op):
        self.type = self.__class__.__name__
        self.max_value = max_value
        self.size_op = size_op
        self.operator = operator
        self.op = op
        self.nb_type = nb_type_dic[nb_type]()
        self.case = None


    def __str__(self):
        return "member of {}".format(self.type)

    def new_case(self):

        lst = []
        for _ in range(self.size_op):
            lst.append(self.nb_type.val(self.max_value))
        lst.sort(reverse=True)

        res = lst[0]
        for i in lst[1:]:
            res = self.op(res, i)

        lst.append(res)

        return lst


    def pr_case(self):
        lst = self.new_case()
        self.case = lst
        lst = [str(x) for x in lst]
        ret_str = self.operator.join(lst[:-1]) + " = ? "
        return ret_str


class Addition(Operation):
    """Addition"""

    def __init__(self, max_value, nb_type, size_op):
        Operation.__init__(self, max_value, nb_type, " + ", add, size_op)

class Soustraction(Operation):
    """Soustraction"""

    def __init__(self, max_value, nb_type, size_op):
        Operation.__init__(self, max_value, nb_type, " - ", sub, size_op)

class Multiplication(Operation):
    """Multplication"""

    def __init__(self, max_value, nb_type, size_op):
        Operation.__init__(self, max_value, nb_type, " X ", mul, size_op)

class Division(Operation):
    """Division"""

    def __init__(self, max_value, nb_type,size_op):
        Operation.__init__(self, max_value, nb_type, " / ", truediv, size_op)


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
    for name, obj in getmembers(modules[__name__]):
        if isclass(obj):
            print(obj)

if __name__ == "__main__":
    print_classes()








