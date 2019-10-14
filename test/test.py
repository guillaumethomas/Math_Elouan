import master_class
from helper import xdict, freeze


def test():
    a = master_class.Addition(50, "Int")
    print(a.__doc__)
    print(a.type)
    c = a.pr_case()
    return c, a

if __name__ == "__main__":
    c, a = test()
    print(c)
    d = master_class.Soustraction(60, "Int")
    print(d.type)
    print(d.pr_case())

    e = xdict(a=7, b=8, c=9)
    e = freeze(d)