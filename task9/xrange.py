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
        val = self.start
        if (self.step > 0) and (val >= self.stop):
            raise StopIteration
        elif (self.step < 0) and (val <= self.stop):
            raise StopIteration
        self.start += self.step
        return val

    def __getitem__(self, elem):
        element = self.start + elem*self.step
        if element >= self.stop:
            raise IndexError("Myxrange object index out of range")
        else:
            return element

    def __len__(self):
        return abs(self.start - self.stop) // abs(self.step)

    def __reversed__(self):
        if (self.step > 0) and (self.start < self.stop) or \
                    (self.step < 0) and (self.start > self.stop):
            if self.step > 0:
                new_stop = self.start - 1    
            else:
                new_stop = self.start + 1
            if self.stop > 0:
                new_start = self.stop - 1
            else:
                new_start = self.stop + 1
            self.step *= -1
            self.start = new_start
            self.stop = new_stop
        return self


def main():
    #for i in Myxrange(1, 10, 2):
    #    print i
    #a = Myxrange(5)
    #print a[1], a[5]
    #q = reversed(Myxrange(5))
    #print next(q)
    #print list(q)
    #x = reversed(Myxrange(35435435543534))
    #print next(x)
    #print len(x)

if __name__ == "__main__":
    main()