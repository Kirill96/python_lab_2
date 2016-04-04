def cached(func):

    def wrapper(*args):
        wrapper.s = ""
        res = 0
        try:
            wrapper.count += 0
        except AttributeError:
            wrapper.count = 0
            wrapper.dct = {}

        for i in xrange(len(args)):
            wrapper.s += str(args[i])
        if wrapper.s in wrapper.dct:
            return wrapper.dct[wrapper.s]
        else:
            res = func(*args)
            wrapper.dct[wrapper.s] = res
            return res
    return wrapper

"""@cached
def _sum(*args):
    su = 0
    for i in args:
        su += i
    return su

print _sum(5, 1), _sum(5, 1, 2), _sum(5, 1, 2)"""
