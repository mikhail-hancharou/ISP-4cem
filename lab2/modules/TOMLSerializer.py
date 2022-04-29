from modules.Serializer import Serializer
from modules.hard_tools import ser
from modules.hard_tools import des
# import pytomlpp
import toml


class TomlSerializer(Serializer):
    def dump(self, obj, file: str):
        output = TomlSerializer.dumps(obj)
        try:
            with open(file, 'w') as f:
                f.write(output)
        except IOError:
            print('File IO Error')
        return output

    def dumps(self, obj):
        return toml.dumps(ser(obj))  # pytomlpp

    def load(self, file):
        try:
            with open(file, 'r') as file:
                return TomlSerializer.loads(file.read())
        except IOError:
            print('File IO Error')

    def loads(self, s):
        str = toml.loads(s)
        return des(str)  # pytomlpp
