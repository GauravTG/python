def show1():
    print("iunside show1")
def show2():
    print("inside show2")
def show3():
    print("inside show3")

def caller(func):
     func()
     
caller(show1)
caller(show2)
caller(show3)