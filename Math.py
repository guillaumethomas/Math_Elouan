# import
"""First program"""
from random import randint
from time import time
import basic
import user_input

# test


def menu():
    """"Menu"""

    print("")
    print("Seattle 2017")
    print("Bonjour Elouan")
    print("Bienvenue dans ton jeu de Math")
    print("Ton Papa")
    print("")
    print("Quels operations veux tu faire ?")
    print("Type:")
    print("'1' for additions")
    print("'2' for soutractions")
    print("'3' for multiplications")
    print("'4' for divisions")
    print("'5' for all of the above")
    print("'x' pour quitter")
    print("")
    inp = user_input.res(6, False)
    print("")
    if inp != 'x':
        return int(inp) - 1
    else:
        print('Au revoir')
        exit()


def operations(oper):
    """"script"""

    start_t = time()
    i = 0
    j = -1

    bool_test = True

    while bool_test:
        j += 1
        xx = oper
        if oper == 4:
            xx = randint(0, 3)

        list_op = basic.to_be_cal(xx, 200)
        operator = list_op[0]
        a = list_op[1]
        b = list_op[2]
        e = list_op[3]

        d = str(a) + operator + str(b) + " = ? "
        print(d)
        c = user_input.res(10000, True)

        if c == 'x':

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

        elif c != 'x':
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
    operations(menu())
