def factory_metaclass(path_of_file):
    class MyMetaClass(type):
        def __new__(mcs, name, bases, dct):
            with open(path_of_file, 'r') as f_read:
                for line in f_read.readlines():
                    lst = line.replace('\n', '=').split('=')
                    dct[lst[0]] = eval(lst[1])
            return super(MyMetaClass, mcs).__new__(mcs, name, bases, dct)
    return MyMetaClass

class MyClass(object):
    __metaclass__ = factory_metaclass("data_for_meta.txt")


def main():
    x = MyClass()
    print x.a
    print x.b
    print x.c
    print MyClass.__dict__

if __name__ == "__main__":
    main()