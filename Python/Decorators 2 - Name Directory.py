def person_lister(f):
    def inner(people): 
        gen = (f(each) for each in sorted(people,key=lambda x:int(x[2])))
        # complete the function
        return gen
    return inner
