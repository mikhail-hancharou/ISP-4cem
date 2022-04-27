from modules.hard_tools import ser


x = 50


def func():
    c = x + 1
    print(f"{c} - is mine")


class MyClass:
    class_v = 10

    def __int__(self):
        print("ggg")

    def cl(self, y):
        return x * (self.class_v - y)


def main():
    # d = { "a": 1, "b": 2 }
    # b = list(d.keys())
    # for i in b:
    #    print(i)
    #print(i for i in b)
    print(ser(func))
    print(ser(MyClass))


if __name__ == '__main__':
    main()
