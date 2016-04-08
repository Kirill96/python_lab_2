class Logger(object):
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if hasattr(attr, '__call__'):

            def newfunc(*args, **kwargs):
                name_class = ''
                tmp = str(type(self))

                for i in xrange(17, len(tmp)-2):
                    name_class += tmp[i]
                result = attr(*args, **kwargs)

                with open('logs_'+ name_class + '.txt', 'a') as file_w:
                    file_w.write(('Method: {0}\nargs: {1}\nkwargs: {2}\n'
                                  'result: {3}\n\n').format(attr,\
                                  args, kwargs, result))

            return newfunc
        else:
            return attr

    def __str__(self):
        name_class = ''
        lst = []
        string = ''
        tmp = str(type(self))

        for i in xrange(17, len(tmp)-2):
            name_class += tmp[i]

        with open('logs_'+ name_class + '.txt', 'r') as file_r:
            lst = file_r.readlines()

        for line in lst:
            string += line

        return string


class Myclass(Logger):
    def my_func(self, num1, num2, num3=1):
        return num1 + num2 + num3


class Aaaaaa(Logger):
    def func(self, arg):
        return arg
    def test(self, arg):
        return arg


#a = Myclass()
#a.my_func(1, 2, num3=1)
#a.my_func(10, 10, num3=10)
#print str(Myclass())
#x = Aaaaaa()
#x.func(2)
#x.func(3)
#x.func(5)
#x.test(1)
#print str(Aaaaaa())
