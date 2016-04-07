class Myxrange(object):

    def __init__(self, *args):
        self.start = 0
        self.stop = 0
        self.step = 1
        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise ValueError("Error input value in xrange!")

    def __iter__(self):
        return self

    def next(self):
        if self.start < self.stop:
            start = self.start
            self.start += self.step
            return start
        else:
            raise StopIteration()

    def __getitem__(self, elem):
        element = self.start + elem*self.step
        if element >= self.stop:
            raise IndexError("Myxrange object index out of range")
        else:
            return element

"""
for i in Myxrange(1, 10, 2):
    print i
a = Myxrange(5)
print a[1], a[5]
"""