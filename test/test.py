import master_class

def test():
    a = master_class.Addition(50, "Int")
    print(a.type)
    c = a.new_case()
    return c

if __name__ == "__main__":
    c = test()
    print(c)
    d = master_class.Soustraction(60, "Int")
    print(d.type)
    print(d.new_case())