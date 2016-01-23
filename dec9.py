def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('Hello')
def now(area):      # now function is equal to a special wrapper, having the return address of the original now().
    print area, '2016-01-23'
#log('Hello') return the decorator function
#decorator(func) return the wrapper function
#wrapper function execute the 'print' statement, and then return the func() function, it is the original now function.

now('Beijing')
print 'The name of function now() is:', now.__name__



