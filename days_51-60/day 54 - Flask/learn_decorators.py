def our_decorator(function):
    def function_wrapper(x):
        # do something before run fuction
        print("before")

        # proper function
        function(x)

        # or run function twiece
        function(x)

        # or do somethni after run function
        print("after \n")

    return function_wrapper



# foo
@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi1")
print("\n")
foo("Hi")


# foo2
def foo2(x):
    print("Hi, foo has been called with " + str(x))

foo2("Hi2")

try:
    # @our_decorator
    foo2("Hi")
except:
    print("we use decorator only when define functions, not when we call")

our_decorator(foo2)("Hi3")
""" this is the same as 
@our_decorator
def foo2(): 
foo2("Hi3")
"""