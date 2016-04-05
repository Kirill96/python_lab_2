class MyMetaClass(type):

    def __new__(mcs, name, bases, dct):
        path_of_file = raw_input("Input path of file: ")
        with open(path_of_file, 'r') as f_read:
            for line in f_read.readlines():
                lst = line.replace('\n', '=').split('=')
                dct[lst[0]] = lst[1]
        return super(MyMetaClass, mcs).__new__(mcs, name, bases, dct)


class MyClass(object):
    __metaclass__ = MyMetaClass

"""
x = MyClass()
print x.a
print x.b
print x.c
"""