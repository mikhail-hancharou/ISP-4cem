from modules.Serializer import Serializer
from modules.hard_tools import ser
from modules.hard_tools import des
import toml


class TomlSerializer(Serializer):
    def dump(self, obj, file: str):
        output = self.dumps(obj)
        #try:
        with open(file, 'w') as f:
            f.write(output)
        # except IOError:
        #    print('File IO Error')
        # return output

    def dumps(self, obj):
        toml_obj = change_tuple_to_list(ser(obj))
        return toml.dumps(toml_obj)

    def load(self, file):
        try:
            with open(file, 'r') as file:
                return self.loads(file.read())
        except IOError:
            print('File IO Error')

    def loads(self, s):
        s = toml.loads(s)
        s = from_toml_obj(s)
        print(s)
        return des(s)


def from_toml_obj(dc):
    dic = dc.copy()
    for k, v in dc.items():
        key = k
        if isinstance(k, str) and k[0] == "(":
            key = str_to_tuple(k)
            dic[key] = dic.pop(k)
        if isinstance(v, dict):  # and len(v) != 1
            dic[key] = from_toml_obj(dic.pop(key))
        if isinstance(v, list):
            dic[key] = from_toml_list(dic.pop(key))
    return dic


def str_to_tuple(s):
    output = list()
    ls = s.split(", ")
    for it in ls:
        el = it
        el = el.replace('(', "")
        el = el.replace(')', "")
        el = el.replace("'", "")
        output.append(el)
    return tuple(output)


def change_tuple_to_list(obj):
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = change_tuple_to_list(v)
        if k == "tuple" or k == "list" or k == "bytes":
            copy_list = list()
            for it in list(v):
                copy_it = it
                if isinstance(it, dict):
                    copy_it = change_tuple_to_list(it)
                copy_list.append(copy_it)
            obj[k] = copy_list
    return obj


def from_toml_list(obj):
    output = list()
    for it in obj:
        copy = it
        if isinstance(it, dict):
            copy = from_toml_obj(it)
        output.append(copy)
    return output

