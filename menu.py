import sys, inspect
from master_class import Addition, Soustraction, Division, Multiplication

def print_classes():
    """Using reflection in python"""
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj.__doc__)

if __name__ == "__main__":
    print_classes()