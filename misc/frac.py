from fractions import Fraction
from random import randint
from misc.basic import to_be_cal


def gen_frac(max_val):

    return Fraction(randint(1, max_val), randint(1, max_val))


def frac_to_be_cal(op, max_val):
    a = gen_frac(max_val)
    b = gen_frac(max_val)
    res_list = to_be_cal(op, max_val, a, b)
    return res_list


if __name__ == "__main__":
    print(frac_to_be_cal(0, 10))
    print(frac_to_be_cal(1, 10))
    print(frac_to_be_cal(2, 10))
    print(frac_to_be_cal(3, 10))
    a = frac_to_be_cal(0, 10)
    