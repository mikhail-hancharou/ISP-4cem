from modules.hard_tools import ser
from modules.hard_tools import des


x = 50


def func():
    c = x + 1
    print(f"{c} - is mine")


def decor():
    def beb():
        print("fff")
    return beb


def factor(f):
    if f > 1:
        return f * factor(f - 1)
    else:
        return f


class MyClass:
    class_v = 10

    def __init__(self):
        print("ggg")

    def cl(self, y):
        return x * (self.class_v - y)


def main():
    '''
    ls = [1, 2, 3, "gg", [4, 5]]
    sls = ser(ls)
    print(sls)
    print(des(sls))

    d = {"a": 1, "b": 2, "c": {1: 3, "e": 4}}
    sd = ser(d)
    print(sd)
    print(des(sd))

    t = ("a", 1, 2, [3, 4])
    st = ser(t)
    print(st)
    print(des(st))

    sb = ser(bytes([50, 100, 76, 72, 41]))
    print(sb)
    print(des(sb))'''
    sf = ser(func)
    print(sf)
    des_func = des(sf)
    des_func()

    sff = ser(decor)
    print(sff)
    des_sff = des(sff)
    test_f = des_sff()
    test_f()

    s_factor = ser(factor)
    test_ff = des(s_factor)
    print(test_ff(3))

    f = lambda c: c * c
    slam = ser(f)
    test_lam = des(slam)
    print(test_lam(10))

    #print(ser(MyClass))


if __name__ == '__main__':
    main()
