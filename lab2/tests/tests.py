import unittest
from modules.JsonSerializerCreator import JsonSerializerCreator
from modules.SerFactory import ParserFactory


def add(x, y):
    return x + y


def factor(f):
    if f > 1:
        return f * factor(f - 1)
    else:
        return f


mul = lambda x, y: x * y


def outer_func():
    def inner_func():
        return "Hello, World!"
    inner_func()


x = 50


class MyClass:
    class_v = 10

    def __init__(self):
        print("ggg")

    def cl(self, y):
        return x * (self.class_v - y)

    @staticmethod
    def br(y):
        return y * y


my_obj = MyClass()


class TestFunc(unittest.TestCase):
    format = {"json": "test_json.json", "toml": "test_toml.toml", "yaml": "test_yaml.yaml"}

    def test_str(self):
        for val in self.format.keys():
            parser = ParserFactory.create_parser(val)
            in_format = parser.dumps(add)
            in_python = parser.loads(in_format)
            self.assertEqual(in_python(1, 2), add(1, 2))

    def test_file(self):
        for k, v in self.format.items():
            parser = ParserFactory.create_parser(k)
            parser.dump(add, v)
            in_python = parser.load(v)
            self.assertEqual(in_python(2, -2), add(2, -2))

    def test_factor(self):
        for val in self.format.keys():
            parser = ParserFactory.create_parser(val)
            in_format = parser.dumps(factor)
            in_python = parser.loads(in_format)
            parsed = in_python
            real = factor
            self.assertEqual(parsed(4), real(4))


class TestClass(unittest.TestCase):
    format = {"json": "test_json.json", "toml": "test_toml.toml", "yaml": "test_yaml.yaml"}

    def test_str(self):
        for val in self.format.keys():
            parser = ParserFactory.create_parser(val)
            in_format = parser.dumps(MyClass)
            in_python = parser.loads(in_format)
            self.assertEqual(in_python.br(1), MyClass.br(1))

    def test_file(self):
        for k, v in self.format.items():
            parser = ParserFactory.create_parser(k)
            in_format = parser.dump(MyClass, v)
            in_python = parser.load(v)
            self.assertEqual(in_python.br(1), MyClass.br(1))


if __name__ == "__main__":
    unittest.main()
