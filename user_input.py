
def res(max,quit):
    bool = True

    while bool is True:
        try:
            y = input("Please enter a number: ")
            x = int(y)
            if x < max:
                bool = False
            else:
                print("Oops!  That was no valid number.  Try again...")
        except ValueError:
            if bool and y == 'x':
                x = y
                break
            else:
                print("Oops!  This is not a number.  Try again...")

    return x

if __name__ == "__main__":
    print("Not supposed to be used directly")