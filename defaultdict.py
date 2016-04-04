class DefaultDict(dict):
    def __getitem__(self, key):
        try:
            return super(DefaultDict, self).__getitem__(key)
        except KeyError:
            self[key] = DefaultDict()
            return self[key]

x = DefaultDict()
x["fjug"][4][5] = 5
x[10][1] = 8
print x
print x[10][1]
