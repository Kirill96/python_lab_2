def cached(func):
    def wrapper(*args, **kwargs):
        s = list(args)
        res = 0
        for key in kwargs:
            s.append((key, kwargs[key]))
        s = tuple(s)
        if s in dct:
            print('Take in cache:', s)
        else:
            print('New result:', s)
            res = func(*args, **kwargs)
            dct[s] = res
        return dct[s]
    dct = {}
    return wrapper


def main():
    @cached
    def _sum(*args, **kwargs):
        su = 0
        for i in args:
            su += i
        for el in kwargs:
            su += kwargs[el]
        return su

    print _sum(5, 1)
    print _sum(5, 1)
    print _sum(5, 1, a=2)
    print _sum(5, 1, a=2)

if __name__ == "__main__":
    main()
