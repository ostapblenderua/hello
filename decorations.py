def announce(f):
    def wrapper():
        print("About to run a function")
        f()
        print("I'm done with that")

    return wrapper
    
@announce
def hello():
    print("'ello world")


hello()