import argparse

class Logger(object):
    def __init__(self):
        self.write_result = True
        self.write_arguments = True
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if hasattr(attr, '__call__'):
            
            def newfunc(*args, **kwargs):
                name_class = type(self).__name__
                result = attr(*args, **kwargs)
                with open('logs_'+ name_class + '.txt', 'a') as file_w:
                    """file_w.write(('Method: {0}\nargs: {1}\nkwargs: {2}\n'
                                  'result: {3}\n\n').format(attr,\
                                  args, kwargs, result))"""
                    if self.write_result and self.write_arguments:
                        file_w.write(('Method: {0}\nargs: {1}\nkwargs: {2}\n'
                                  'result: {3}\n\n').format(attr,\
                                  args, kwargs, result))
                    elif not self.write_result and not self.write_arguments:
                        file_w.write(('Method: {0}\n').format(attr))
                    elif self.write_result and not self.write_arguments:
                        file_w.write(('Method: {0}\nresult: {1}\n\n')\
                                     .format(attr, result))
                    elif not self.write_result and self.write_arguments:
                        file_w.write(('Method: {0}\nargs: {1}\nkwargs: '
                                      '{2}\n\n').format(attr, args, kwargs))
            return newfunc
        else:
            return attr

    def __str__(self):
        lst = []
        string = ''
        name_class = type(self).__name__

        with open('logs_'+ name_class + '.txt', 'r') as file_r:
            lst = file_r.readlines()

        for line in lst:
            string += line

        return string


class Myclass(Logger):
    def my_func(self, x, y, z=1):
        return x + y + z


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=int, help='First argument of my_func')
    parser.add_argument('-y', type=int, help='Second argument of my_func')
    parser.add_argument('-z', type=int, help='Third argument of my_func')
    parser.add_argument('--write-result', action='store_true', default=False,
        help='Write result if True')
    parser.add_argument('--write-arguments', action='store_true', default=False,
        help='Write arguments if True')
    param = parser.parse_args()

    a = Myclass()
    a.write_result = param.write_result
    a.write_arguments = param.write_arguments
    a.my_func(param.x, param.y, z=param.z)
    print str(Myclass())

if __name__ == '__main__':
    main()
