def wrapper(f):
    def fun(l):
        # complete the function 
        arr = ["+91 {} {}".format(each[-10:-5],each[-5:]) for each in l] 
        f(arr)
    return fun
