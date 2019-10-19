# import
"""First program"""
from random import randint
from time import time
from misc.basic import to_be_cal
from misc.frac import frac_to_be_cal
from misc.user_input import res

# test


def menu(exit_char):
    """"Menu"""

    print("\nSeattle 2017 \nBonjour Elouan \n ")
    print("Bienvenue dans ton jeu de Math \n Ton Papa \n\n")
    print("Quels operations veux tu faire ?")
    print("Type:")
    print("'1' for additions")
    print("'2' for soutractions")
    print("'3' for multiplications")
    print("'4' for divisions")
    print("'5' for all of the above")
    print("'6' for fractions")
    print("'q' pour quitter\n\n")
    inp = res(7, False)
    print("")
    if inp != exit_char:
        return [int(inp) - 1, exit_char]
    else:
        print('Au revoir')
        return None


def operations(oper, exit_char):
    """"script"""

    start_t = time()
    i = 0
    j = -1

    bool_test = True
    # max value to be randomly generated
    val = 9999

    funct = to_be_cal
    if oper == 5:
        funct = frac_to_be_cal
        oper = 4

    while bool_test:
        j += 1
        xx = oper

        if oper == 4:
            xx = randint(0, 3)

        list_op = funct(xx, val)
        operator = list_op[0]
        a = list_op[1]
        b = list_op[2]
        e = list_op[3]

        d = str(a) + operator + str(b) + " = ? "
        print(d)
        c = res(2 * val, exit_char)

        if c == exit_char:

            if j > 0:
                final_t = time() - start_t
                time_per_op = round(final_t / j, 2)
                final_t = ' en ' + str(round(final_t, 0)) + ' secondes'
                time_per_op = str(time_per_op) + ' secondes par operation'

                print("")
                print('Ton score est ' + str(i) + " sur " + str(j) + final_t)
                print('soit environ ' + time_per_op)

            print("Au revoir Elouan !")
            print("")
            bool_test = False

        elif c != exit_char:
            c = int(c)
            if c == e:
                print("")
                print ("Bravo + 1 point")
                print("")
                i += 1

            else:

                print("C'est faux !")
                print("la bonne reponse est :" + str(e))
                print("")


if __name__ == "__main__":
    exit_char = 'q'
    inp = menu(exit_char)
    if inp is not None:
        operations(*inp)
