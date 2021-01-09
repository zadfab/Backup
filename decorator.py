def outer_div(func):
    def inner(x,y):
        if(x<y):
            x,y = y,x
        return func(x,y)
    return inner
# syntax of generator
@outer_div
def divide(x,y):
    print(x/y)

divide(2,400)