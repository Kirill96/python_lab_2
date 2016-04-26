
class BaseField(object):
    value_type = None

class StringField(BaseField):
    value_type = str

class IntField(BaseField):
    value_type = int

class BoolField(BaseField):
    value_type = bool

class ModelCreator(type):

    def __init__(cls, name, bases, dct):
        for attr in dct:
            if isinstance(dct[attr], BaseField):
                def setter_gen(attr_copy):
                    def setter(self, value):
                        if not isinstance(value, dct[attr_copy].value_type):
                            raise TypeError("{} value must be a {}, not a {}!"\
                                .format(attr_copy, dct[attr_copy].value_type,\
                                value.__class__))
                        self.__dict__["_" + attr_copy] = value
                    return setter

                def getter_gen(attr_copy):
                    def getter(self):
                        return self.__dict__["_" + attr_copy]
                    return getter

                setattr(cls, attr, property(getter_gen(attr), setter_gen(attr)))

        super(ModelCreator, cls).__init__(name, bases, dct)


class Model(object):
    __metaclass__ = ModelCreator

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

        super(Model, self).__init__()


def main():
    class UserModel(Model):
        id = IntField()
        name = StringField()
        is_student = BoolField()

        def __str__(self):
            return "[{}] {} (is_student={})".format(self.id, self.name, self.is_student)

    u = UserModel(name='Kirill', id=10, is_student=True)
    u2 = UserModel(name='Andrey', id=100, is_student=False)
    print u, '\n', u2
    try:
        #u2.is_student = 'net'
        #u.name = 2
        u.id = 'sfsdf'
    except Exception, e:
        print str(e)

if __name__ == "__main__":
    main()