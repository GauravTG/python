def myfun(char):
    if char.isupper():
        return char.lower
    elif char.islower:
        return char.upper()
    else:
        print("enter a vald number")
        
result=myfun("a")
print("your toggles char is ",result)
    