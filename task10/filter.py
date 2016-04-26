class Filter(object):

    def __init__(self, arg):
        self.obj = [el for el in arg]

    def __iter__(self):
        return iter(self.obj)

    def __str__(self):
        return str(self.obj)

    def filtration(self, function):
        length = len(self.obj)
        for i in range(length):
            if function(self.obj[i]):
                yield self.obj[i]
            else:
                continue


def func(elem):
    if elem == 2 or elem == 4:
        return True
    else:
        return False


def main():
    a = Filter([1, 2, 3, 4])
    x = Filter({1: 2, 4: 1})
    print list(a.filtration(func))
    print list(a.filtration(func))
    print list(x.filtration(func))
    print a, x

    for i in a:
        print i

if __name__ == "__main__":
    main()