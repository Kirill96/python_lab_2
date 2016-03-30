import math

class Vector(object):

    def __init__(self, *args):
        self.sum = 0
        self.length = 0
        self._list = []
        for arg in args:
            self._list.append(arg)

    def __add__(self, obj):
        vect = Vector()

        if len(self._list) < len(obj):
            for elem in range(len(self._list)):
                vect.append_(self._list[elem] + obj[elem])
            for elem in range(len(self._list), len(obj)):
                vect.append_(obj[elem])
        elif len(self._list) > len(obj):
            for elem in range(len(obj)):
                vect.append_(self._list[elem] + obj[elem])
            for elem in range(len(obj), len(self._list)):
                vect.append_(self._list[elem])
        else:
            for elem in range(len(self._list)):
                vect.append_(self._list[elem] + obj[elem])

        return vect

    def __sub__(self, obj):
        vect = Vector()

        if len(self._list) < len(obj):
            for elem in range(len(self._list)):
                vect.append_(self._list[elem] - obj[elem])
            for elem in range(len(self._list), len(obj)):
                vect.append_(-obj[elem])
        elif len(self._list) > len(obj):
            for elem in range(len(obj)):
                vect.append_(self._list[elem] - obj[elem])
            for elem in range(len(obj), len(self._list)):
                vect.append_(self._list[elem])
        else:
            for elem in range(len(self._list)):
                vect.append_(self._list[elem] - obj[elem])

        return vect

    def __mul__(self, obj):
        vect = Vector()
        if type(vect) != type(obj):
            for elem in range(len(self._list)):
                vect.append_(self._list[elem] * obj)
        else:
            for elem in range(len(self._list)):
                vect.append_(self._list[elem] * obj[elem])

        return vect

    def __eq__(self, obj):

        if len(self._list) != len(obj):
            return False
        for elem in range(len(self._list)):
            if self._list[elem] != obj[elem]:
                return False

        return True

    def  __ne__(self, obj):

        if len(self._list) != len(obj):
            return True
        for elem in range(len(self._list)):
            if self._list[elem] != obj[elem]:
                return True

        return False

    def len(self):
        for elem in range(len(self._list)):
            self.sum += pow(self._list[elem], 2)
        self.length = math.sqrt(self.sum)

        return self.length

    def __str__(self):
        self.str = "{"
        for elem in range(len(self._list)):
            self.str += str(self._list[elem])
            if elem != len(self._list) - 1:
                self.str += ", "
        self.str += "}"
        return self.str

    def append_(self, elem):
        self._list.append(elem)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, elem):
        return self._list[elem]

    def __setitem__(self, elem, value):
        self._list[elem] = value

v1 = Vector(1, 2, 3)
v2 = Vector(2, 4, 6)
v3 = Vector(1, 2, 3, 5)
v4 = Vector(2, 4, 6)

summ = v1 + v2
subb = v1 - v2
mul = v1 * v2
mul1 = v2 * v2
a = v1 - v3
b =  v3 - v1
c =  v1 - v2

print v2.len()
print v2 + v1
print v1 - v2
print v1 * v2
print v1 * 10
print v1 == v2
print v1 != v2
print v2 == v4
print v3[3]
print v3
print a, b, c
