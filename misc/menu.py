import sys, inspect
from master_class import Addition, Soustraction, Division, Multiplication

def print_classes(max_int):
    dic = dict()
    """Using reflection in python"""
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            # print(obj.__doc__)
            # dic[obj.__name__] = obj(max_int, "Int")
            # dic[obj.__name__] = obj(max_int, "Frac")
            dic[obj.__name__] = obj(max_int, "Dec")

    return dic

def ui(max_int):
    print("\nOn aime les Maths!\nPar Guillaume THOMAS (Papa)\nPour Elouan\n2019\n")

    # Reflection to generate menu:
    dic = print_classes(max_int)

    for value in dic.values():
        print(value.type)
        print(value.pr_case())

    return dic


if __name__ == "__main__":
    dic = ui(500)
