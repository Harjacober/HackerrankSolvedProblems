class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        a1,a2,a3 = self.x,self.y,self.z
        b1,b2,b3 = no.x, no.y, no.z
        x = b1-a1 
        y = b2-a2 
        z = b3-a3 
        return Points(x,y,z)
    def dot(self, no):
        a1,a2,a3 = self.x,self.y,self.z
        b1,b2,b3 = no.x, no.y, no.z
        return (a1*b1)+(a2*b2)+(a3*b3)

    def cross(self, no):
        a1,a2,a3 = self.x,self.y,self.z
        b1,b2,b3 = no.x, no.y, no.z
        x = (a2*b3)-(a3*b2)
        y = (a3*b1)-(a1*b3)
        z = (a1*b2)-(a2*b1)
        return Points(x,y,z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
