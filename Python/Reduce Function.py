def product(fracs):
    func = lambda x,y:x*y 
    t = reduce(func ,fracs)
    return t.numerator, t.denominator
