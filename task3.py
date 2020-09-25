# Write decorator that measures function execution time
# and print it to output console.


from time import clock


def execution_time(function):
    def _execution_time(*args, **kw):
        # time before calling the function
        current_time = clock()
        rez = function(*args, **kw)  # function call
        # calculate the time difference
        dt = clock() - current_time
        print('Час виконання функції %1.5f сек' % dt)
        return rez
    return _execution_time
