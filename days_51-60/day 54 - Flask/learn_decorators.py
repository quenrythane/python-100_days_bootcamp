def our_decorator(function):
    def function_wrapper(x):
        # do something before run fuction
        print("before")

        # proper function
        function(x)

        # or run function twiece
        function(x)

        # or do somethni after run function
        print("after")

    return function_wrapper



# foo
@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")
print("\n")
foo("Hi")


# foo2
def foo2(x):
    print("Hi, foo has been called with " + str(x))

foo2("Hi")

try:
    @our_decorator
    foo2("Hi")
except Exception as e:
    print(e)
    print("we use decorator only when define functions, not when we call")


