import sys, inspect
from master_class import Addition, Soustraction, Division, Multiplication

def print_classes(max_int):
    dic = dict()
    """Using reflection in python"""
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj.__doc__)
            dic[obj.__name__] = obj(max_int, "Int")

    return dic

if __name__ == "__main__":
    dic = print_classes(50)

    for value in dic.values():
        print(value.type)
        print(value.pr_case())  