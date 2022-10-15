def our_decorator(xd):
    def function_wrapper(x):
        # do something before run fuction
        print("before")

        # proper function
        xd(x)

        # or run function twiece
        xd(x)

        # or do something after run function
        print("after")

    return function_wrapper


@our_decorator
def foo(name):
    print("Hi, foo has been called with " + str(name))


print(foo("Artur"))
