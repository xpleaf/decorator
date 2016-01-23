def log(text):
    def decorator(func):
        def wrapper():
            print '%s %s():' % (text, func.__name__)
            return func()
        return wrapper
    return decorator


def now():
    print '2016-01-23'


now = log('Hello')(now) # now is equal to a special wrapper, having the return address of the original now().
      #log('Hello') return the decorator function
      #decorator(func) return the wrapper function
      #wrapper function execute the 'print' statement, and then return the func() function, it is the original now function.

now()
print 'The name of function now() is:', now.__name__



