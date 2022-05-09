from modules.Serializer import Serializer
from modules.hard_tools import ser
from modules.hard_tools import des
import yaml


class YamlSerializer(Serializer):
    def dump(self, obj, fp: str):
        ser_obj = self.dumps(obj)
        try:
            with open(fp, 'w') as f:
                f.write(ser_obj)
        except IOError:
            print("An IOError has occurred!")
        return ser_obj

    def dumps(self, obj):
        yaml_obj = change_tuple_to_list(ser(obj))
        # yaml = func_convert(yaml_obj)
        return yaml.dump(yaml_obj)

    def load(self, fp):
        try:
            with open(fp, 'r') as f:
                script = f.read()
        except IOError:
            print(f"An IOError has occurred: failed to open {fp}")
            return
        return self.loads(script)

    def loads(self, s):
        obj = dict()
        try:
            obj = yaml.safe_load(s)
        except yaml.YAMLError as exc:
            print(exc)
        return des(obj)

    '''def dumps(self, obj: object, dumper=yaml.Dumper):
        return yaml.dumps(ser(obj), Dumper=dumper)

    def dump(self, obj: object, fp: str, dumper=yaml.Dumper):
        with open(fp, "w") as file:
            file.write(self.dumps(obj, dumper=dumper))

    def loads(self, data: str, loader=yaml.FullLoader):
        return from_dict(yaml.load(data, Loader=loader))

    def load(self, fp: str, loader=yaml.FullLoader):
        with open(fp, "r") as file:
            return self.loads(file.read(), loader=loader)'''


def change_tuple_to_list(obj):
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = change_tuple_to_list(v)
        if k == "tuple" or k == "list" or k == "bytes":
            copy = []
            for it in list(v):
                copy.append(change_tuple_to_list(it))
            obj[k] = copy
    return obj


'''def func_convert(obj):
    if "__func__" in obj.keys() and obj["__func__"]["__name__"] in obj["__func__"]["__globals__"].keys():
        if obj["__name__"] in obj["__globals__"]:
            flag = True'''
