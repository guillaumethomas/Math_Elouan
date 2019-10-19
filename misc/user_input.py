
def res(maxi,quit):
    bool = True

    while bool is True:
        try:
            y = input("Please enter a number: ")
            x = int(y)
            if x < maxi:
                bool = False
            else:
                print("Oops!  That was no valid number.  Try again...")
        except ValueError:
            if bool and y == quit:
                x = y
                break
            else:
                print("Oops!  This is not a number.  Try again...")
        '''
        except KeyboardInterrupt:
                print("press 'q' next time to leave this program")
        '''
    return x

if __name__ == "__main__":
    print("Not supposed to be used directly")