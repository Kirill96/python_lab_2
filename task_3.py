class MyException(TypeError):
    def __init__(self, value):
        super(MyException, self).__init__()
        self.value = value
    def __str__(self):
        return repr(self.value)


def to_json(obj, raise_unknown=False):

    string = ""
    i = 0
    if type(obj) == type({}):
        string += "{"
        for elem in obj:
            i += 1
            if type(obj[elem]) == type({}) or type(elem) == type([])\
                                      or type(elem) == type(()):
                string += to_json(elem, raise_unknown)
                string += ": " + to_json(obj[elem], raise_unknown)
                if i != len(obj):
                    string += ", "
            else:
                string += to_json(elem, raise_unknown)
                string += ": " + to_json(obj[elem], raise_unknown)
                if i != len(obj):
                    string += ", "
        return string + "}"

    elif type(obj) == type([]) or type(obj) == type(()):
        string += "["
        for elem in obj:
            i += 1
            if type(elem) == type([]) or type(elem) == type(())\
                                      or type(elem) == type({}):
                string += to_json(elem, raise_unknown)
                if i != len(obj):
                    string += ", "
            else:
                string += to_json(elem, raise_unknown)
                if i != len(obj):
                    string += ", "
        return string + "]"

    elif type(obj) == int:
        string += str(obj)
        return string

    elif type(obj) == long:
        string += str(obj)
        return string

    elif type(obj) == float:
        string += str(obj)
        return string

    elif type(obj) == str or type(obj) == unicode:
        string += '"' + obj + '"'
        return string

    elif obj == True:
        return "true"

    elif obj == False:
        return "false"

    elif obj == None:
        return "null"

    else:
        if raise_unknown == True:
            type_obj = type(obj)
            raise MyException("Attempt to convert an unknown type: "\
                             + str(type_obj))

"""
class A(object):
    def __init__(self, arg):
        super(A, self).__init__()
        self.arg = arg

x = A(4)
        
lst = [1, {"a": 1}, 5, "434", 'ewe', [{"fsd": "fd"}], [[1, 3, 'dsa'], ("d", "a")]]
f = {"foo": 1, "dct": {"asd": 2}}
a = {1: 4, "d": 3}
d = {True: {False: None, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}
print to_json(A, True)"""
