def add_100_decorator(function):
    def wrapper(parameter):
        number = function(parameter)
        result = 100 + number
        return result

    return wrapper

@add_100_decorator
def new_function(number):
    return number


print(new_function(5))
