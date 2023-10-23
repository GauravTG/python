def add():
    print("add fiunction")
def delete():
    print("delete function")
def modify():
    print("modify function")

num=int(input("enter a number"))

match num:
    case 1:
        add()
    case 2:
        delete()
    case 3:
        modify()
    case __annotations__:
        print("enter a vaild number")
    