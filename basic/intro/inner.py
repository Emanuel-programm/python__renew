def outer():
    print("In Outer function")

    def inner(num):
        print("In the inner function",num)
    
    # inner()
    return inner



something=outer()

something(5)