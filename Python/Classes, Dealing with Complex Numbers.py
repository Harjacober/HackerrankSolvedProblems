

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary 
    def __add__(self, no):
        a1,b1,a2,b2 = self.real,self.imaginary,no.real,no.imaginary
        a = a1+a2
        b = b1+b2
        return Complex(a,b)
    def __sub__(self, no):
        a1,b1,a2,b2 = self.real,self.imaginary,no.real,no.imaginary
        a = a1-a2
        b = b1-b2
        return Complex(a,b)
    def __mul__(self, no):
        a1,b1,a2,b2 = self.real,self.imaginary,no.real,no.imaginary
        a = (a1*a2)-(b1*b2)
        b = (a1*b2)+(a2*b1)
        return Complex(a,b)
    def __truediv__(self, no):
        a1,b1,a2,b2 = self.real,self.imaginary,no.real,no.imaginary
        a = ((a1*a2)+(b1*b2))/(pow(a2,2)+pow(b2,2))
        b = ((a2*b1)-(a1*b2))/(pow(a2,2)+pow(b2,2))
        return Complex(a,b)
    def mod(self):
        a1,b1 = self.real,self.imaginary
        a = pow((a1**2)+(b1**2), 0.5)
        return Complex(a,0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
