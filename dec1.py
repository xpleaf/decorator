def log(func):
    def wrapper():
        print 'call %s():' % func.__name__
        return func()
    return wrapper


def now():
    print '2016-01-23'


now = log(now)


now()
print 'The name of function now() is:', now.__name__