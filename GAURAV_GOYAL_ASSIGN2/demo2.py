def outer():
    def inner():
        print("gaurav is great")
    print("gaurav is super great")
    return inner

outer()()