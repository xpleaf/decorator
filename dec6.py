def log(func):
    def wrapper(*args, **kwargs):
        print 'call %s():' % func.__name__
        return func(*args, **kwargs)
    return wrapper


@log
def now1(area):
    print area, '2016-01-23'


now1('Beijing')
print 'The name of function now1() is:', now1.__name__
print "=" * 25


@log
def now2(area, thing):
    print area, thing, '2016-01-23'


now2('Beijing', 'eating')
print 'The name of function now2() is:', now2.__name__