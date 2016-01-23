def log(func):
    def wrapper():
        print 'call %s():' % func.__name__
        return func()
    return wrapper


@log
def now():
    print '2016-01-23'


now()
print 'The name of function now() is:', now.__name__