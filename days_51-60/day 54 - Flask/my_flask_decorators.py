def make_bold(function):
    def wrapped():
        return f"<b>{function()}</b>"
    return wrapped


def make_emphasis(function):
    def wrapped():
        return f"<em>{function()}</em>"
    return wrapped


def make_underlined(function):
    def wrapped():
        return f"<u>{function()}</u>"
    return wrapped


def is_woman(function):
    def wrapped2(*args):
        if args[0][-1] == "a":
            name = f"Mrs {args[0].capitalize()}"
            function(name)
        else:
            name = f"Mr {args[0].capitalize()}"
            function(name)
    return wrapped2


@is_woman
def tak(name):
    print("Hi", name)


if __name__ == "main":
    tak("arta")
    tak("art")
