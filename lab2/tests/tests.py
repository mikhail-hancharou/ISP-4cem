import unittest
from modules.JsonSerializerCreator import JsonSerializerCreator
from modules.SerFactory import ParserFactory


def add(x, y):
    return x + y


mul = lambda x, y: x * y


def outer_func():
    def inner_func():
        return "Hello, World!"
    inner_func()


class Auto:
    mark = 'BMV'
    engine_value = 2.0

    def __init__(self, mark, eng_val):
        self.mark = mark
        self.components = ['wheels', 'body', 'engine']
        self.engine_value = eng_val

    def noise(self):
       return "Rrrrr. I am {:}. My engine value is {:} liter(s)".format(self.mark, self.engine_value)


car = Auto('BMV', 2.5)


class TestFunc(unittest.TestCase):
    format = ["json", "toml", "yaml"]

    def test_str(self):
        for val in self.format:
            parser = ParserFactory.create_parser(val)
            in_format = parser.dumps(add)
            in_python = parser.loads(in_format)
            self.assertEqual(in_python(1, 2), add(1, 2))

    def test_file(self):
        for val in self.format:
            parser = ParserFactory.create_parser(val)
            parser.dump(add)
            in_python = parser.load()
            self.assertEqual(in_python(2, -2), add(2, -2))
