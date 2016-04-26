import random

class SingletonMeta(type):
    def __init__(cls, name, bases, dct):
        super(SingletonMeta, cls).__init__(name, bases, dct)
        cls.instance = None
    def __call__(self, *args, **kw):
        if self.instance is None:
            self.instance = super(SingletonMeta, self).__call__(*args, **kw)
        return self.instance


class Singleton(object):
    __metaclass__ = SingletonMeta

    def __init__(self):
        self.id = random.randint(10, 100)

    def __str__(self):
        return 'My id: ' + str(self.id)


for _ in range(10):
    print(Singleton())
