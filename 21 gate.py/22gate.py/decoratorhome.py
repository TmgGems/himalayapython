def smart_sub(subt):
    def inner(a,b):
         
        if a<b:
            a,b=b,a
        return subt(a,b)
    return inner


def sub(a,b):
    print(a-b)

a=smart_sub(sub)
a(2,4)