from modules.JsonSerializer import JsonSerializer
from modules.hard_tools import ser
from modules.hard_tools import des


x = 50


class Test:
    per = 10


def class_f(self):
    print(self.per)


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


def add(c, y):
    return c + y


class MyClass:
    class_v = 10

    def __init__(self):
        print("ggg")

    def cl(self, y):
        return x * (self.class_v - y)

    @staticmethod
    def br(y):
        return y * y


def main():
    # ser types
    '''ls = [1, 2, 3, "gg", [4, 5]]
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

    # ser func
    '''sf = ser(func)
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
    print(test_lam(10))'''

    # ser class
    '''s_cl = ser(MyClass)
    print(s_cl)
    test_cl = des(s_cl)
    print(test_cl.__dict__)
    print(MyClass.__dict__)
    print(test_cl.cl(5))
    test_obj = test_cl()
    print(test_obj.cl(5))
    print(test_cl.class_v)
    print(MyClass.br(5))
    print(test_cl.br(5))'''

    # ser obj
    '''obj = MyClass()
    s_obj = ser(obj)
    print(s_obj)
    test_obj = des(s_obj)
    print(test_obj.br(5))
    print(obj.cl(5))
    print(test_obj.__dict__)
    print(test_obj.cl(5))'''

    js = JsonSerializer()
    # des types
    '''d = {"a": 1, "c": 2, "b": 3}
    print(ser(d))
    dum = js.dumps(d)
    print(dum)
    print(js.loads(dum))

    ll = [1, 2]
    d = {"b": ll, "a": 4}
    dums = js.dumps(d)
    print(dums)
    print(js.loads(dums))'''
    '''ll = [1, 2]
    dd = {"b": tuple(ll), "a": 4}
    dumt = js.dumps(dd)
    print(dumt)
    print(js.loads(dumt))'''
    '''ddd = {"a": 1, "b": 2}
    dumd = js.dumps(ddd)
    print(dumd)
    print(js.loads(dumd))'''

    print(ser(func))
    dump_f = js.dumps(func)
    print(dump_f)
    des_func = js.loads(dump_f)
    des_func()

    print(ser(MyClass))
    dump_cl = js.dumps(MyClass)
    print(dump_cl)
    des_class = js.loads(dump_cl)
    print(des_class.cl(5))

    obj = MyClass()
    print(ser(obj))
    dumps_obj = js.dumps(obj)
    print(dumps_obj)
    des_obj = js.loads(dumps_obj)
    print(des_obj.br(5))
    print(des_obj.cl(5))

    print(ser(add))
    dump_add = js.dumps(add)
    print(dump_add)
    des_add = js.loads(dump_add)
    print(des_add(3, 4))


if __name__ == '__main__':
    main()
