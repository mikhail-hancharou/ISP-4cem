import codecs
import dis
import inspect
import opcode
import re


def ser(obj):  # serialize
    ser_obj = pre_ser(obj)
    # output = tuple((i, ser_obj[i]) for i in ser_obj)
    return ser_obj
    # return tuple((i, ser_obj[i]) for i in ser_obj)


def pre_ser(obj):
    if isinstance(obj, int | float | str | bool | type(None)):
        return basic_type_ser(obj)
    elif isinstance(obj, list | tuple | bytes):
        return tl_ser(obj)
    elif isinstance(obj, dict):
        return dict_ser(obj)
    # elif inspect.iscode(obj):
        # return serialize_code(obj)
    elif inspect.isfunction(obj):  # inspect.isfunction(obj):
        return ser_func(obj)
    elif inspect.isclass(obj):
        return ser_class(obj)
    else:
        return serialize_prop(obj)


def basic_type_ser(obj):  # str & None & bool & int & float
    temp_dict = dict()
    if isinstance(obj, str):
        temp_dict["str"] = obj
    elif isinstance(obj, type(None)):
        temp_dict["None"] = obj
    elif isinstance(obj, bool):
        temp_dict["bool"] = obj
    elif isinstance(obj, int):
        temp_dict["int"] = obj
    elif isinstance(obj, float):
        temp_dict["float"] = obj
    return temp_dict


def tl_ser(obj):  # tuple & list $ bytes
    temp_dict = dict()
    if isinstance(obj, list):
        temp_dict["list"] = tuple(ser(el) for el in obj)
    elif isinstance(obj, tuple):
        temp_dict["tuple"] = tuple(ser(el) for el in obj)
    else:
        temp_dict["bytes"] = tuple(ser(el) for el in obj)
    return temp_dict


def dict_ser(obj):
    temp_dict = dict()
    temp_dict["dict"] = {}
    # for pair in obj:
    #    temp_dict["dict"][pre_ser(pair)] = pre_ser(obj[pair])
    temp_dict["dict"] = tuple((ser(pair), ser(obj[pair])) for pair in obj)
    return temp_dict


def serialize_code(obj):
    main_key = "code"
    ans = dict()
    ans[main_key] = {}
    
    attr = inspect.getmembers(obj)
    attr = [i for i in attr if not callable(i[1])]
    for i in attr:
        key = ser(i[0])
        val = ser(i[1])
        ans[main_key][ser(i[0])] = ser(i[1])
    ans[main_key] = tuple((k, ans[main_key][k]) for k in ans[main_key])

    return ans


def serialize_function(obj):
    FAT = [  # Function ATtr.
        "__code__",
        "__name__",
        "__defaults__",
        "__closure__",
        "__dir__",
        "__format__"
    ]
    main_key = "function"
    ans = dict()
    ans[main_key] = {}
    attr = inspect.getmembers(obj)
    attr = [i for i in attr if i[0] in FAT]
    for i in attr:
        key = ser(i[0])
        value = ser(i[1])
        ans[main_key][ser(i[0])] = ser(i[1])
        # key = pre_ser(i[0])
        # value = pre_ser(i[1])
        # if i[0] != "__closure__":
        # else:
        #    value = pre_ser(None)

        if i[0] == "__code__":
            key = ser("__globals__")
            ans[main_key][key] = {}
            names = i[1].__getattribute__("co_names")
            glob = obj.__getattribute__("__globals__")
            glob_dict = {}
            for name in names:
                if name == obj.__name__:
                    glob_dict[name] = obj.__name__
                elif name in glob and not inspect.ismodule(name) and name not in __builtins__:
                    glob_dict[name] = glob[name]
            ans[main_key][key] = ser(glob_dict)

    ans[main_key] = tuple((k, ans[main_key][k]) for k in ans[main_key])
    return ans


def nesting(level: int) -> str:
    result = ""
    for i in range(level):
        result += "\t"
    return result


def serialize_prop(obj) -> str:
    return f"{obj}"


def glob_variables(func):
    gl_vars = {}
    for current_gl in func.__code__.co_names:  # search in used global variables
        if current_gl in func.__globals__:  # check if they are visible
            gl_vars[current_gl] = pre_ser(func.__globals__[current_gl])
    return gl_vars


# {
#   "__func__" :
#       {
#       "__name__": obj.__name,
#       "__globals__": {{:}, ...},
#       "__args__": {{:}, ...},
#       }
# }


def ser_func(obj):
    output = dict()
    args = dict()
    cycle = [c for c in obj.__code__.__dir__() if c.startswith('co_')]
    for c in cycle:
        attr = getattr(obj.__code__, c)
        if isinstance(attr, bytes):
            attr = codecs.decode(attr, 'raw_unicode_escape')
        args[c] = pre_ser(attr)  # built-in method AS

    m_key = "__func__"
    output[m_key] = {"__name__": obj.__name__,
                     "__globals__": glob_variables(obj),
                     "__args__": args}

    return output


# {
#   "__class__" :
#       {
#       "__name__": obj.__name,
#       "__globals__": {{:}, ...},
#       "__args__": {{:}, ...},
#
#
#
#
#       }
# }


def ser_class(obj):
    output = dict()
    m_key = "__class__"
    output[m_key] = {'__name__': obj.__name__}
    attrs = [i for i in dir(obj) if not i.startswith('__') or inspect.isfunction(getattr(obj, i))]
    for attr in attrs:
        attr_value = getattr(obj, attr)
        output[attr] = pre_ser(attr_value)
    return output


def serialize_instance(instance_obj):
    ans = dict()
    type = re.search(r"\'(\w+)\'", str(type(instance_obj))).group(1)
    ans[type] = {}
    members = inspect.getmembers(instance_obj)
    members = [i for i in members if not callable(i[1])]
    for i in members:
        key = ser(i[0])
        val = ser(i[1])
        ans[type][key] = val
    ans[type] = tuple((k, ans[type][k]) for k in ans[type])

    return ans

    '''    if inspect.isfunction(obj):
        fields['globals'] = {}
        for instr in dis.get_instructions(obj):
            if instr.opcode in globals_opcodes:
                if instr.argval != 'print':
                    fields['globals'][instr.argval] = obj.__globals__[instr.argval]'''