#Basic Operations
from random import randint
''''

    print("1 for additions")
    print("2 for soutractions")
    print("3 for multiplications")
    print("4 for divisions")


'''
def to_be_cal(op,max_int):
    op_type=[' + ', ' - ', ' x ', ' / ']

    a=randint(1,max_int)
    b=randint(1,max_int)

    if b >= a:
        a, b = b, a

    op_list = [(a + b), (a - b), (a * b), (a // b)]

    res_list = []
    res_list.append(op_type[op])
    res_list.append(a)
    res_list.append(b)
    res_list.append(op_list[op])

    return res_list

if __name__ == "__main__":
    print("Not meant to be called individually")

