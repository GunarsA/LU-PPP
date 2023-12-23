
def do_twice(func):

    def wrapper():
        func()
        func()

    # returns the wrapper funcion
    return wrapper
