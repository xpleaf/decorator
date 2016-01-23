def log(func):
    def wrapper(area):
        print 'call %s():' % func.__name__
        return func(area)
    return wrapper


@log
def now(area):
    print area, '2016-01-23'


now('Beijing')
print 'The name of function now() is:', now.__name__