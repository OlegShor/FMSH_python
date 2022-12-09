from math import sqrt, acos, sin, cos, pi


class compl():
    def __init__ (self, real, imaginary):
        self.r = real
        self.i = imaginary

    #+
    def __add__(self, other):
        if isinstance(other, compl):
            return compl(self.r + other.r, self.i + other.i)
        elif isinstance(other, int | float):
            return compl(self.r + other, self.i)
    def __radd__(self, other):
        if isinstance(other, int | float):
            return compl(self.r + other, self.i)
    
    #-
    def __sub__(self, other):
        if isinstance(other, compl):
            return compl(self.r - other.r, self.i - other.i)
        elif isinstance(other, int | float):
            return compl(self.r - other, self.i)
    def __rsub__(self, other):
        if isinstance(other, int | float):
            return compl(self.r - other, self.i)

    #*
    def __mul__(self, other):
        if isinstance(other, compl):
            return compl(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)
        elif isinstance(other, int | float):
            return compl(self.r * other, self.i * other )
    def __rmul__(self, other):
        if isinstance(other, int | float):
            return compl(self.r * other, self.i * other )

    #/
    def __truediv__(self, other):
        if isinstance(other, compl):
            return compl((self.r * other.r + self.i * other.i) / (other.r**2 + other.i**2), (self.i * other.r - self.r * other.i) / (other.r**2 + other.r**2))
        elif isinstance(other, int | float):
            return compl(self.r / other, self.i / other )
    def __rtruediv__(self, other):
        if isinstance(other, int | float):
            return compl(self.r / other, self.i / other )



    #**
    def __pow__(self, other):
        if isinstance(other, int | float):
            a = sqrt(self.r ** 2 + self.i ** 2)
            return compl((a ** other)*cos(acos(self.r / a)*other) , (a ** other) * sin(acos(self.r / a)*other))
    
    #root
    def root(self, other):
        if isinstance(other, int | float):
           rot = []
           a = sqrt(self.r ** 2 + self.i ** 2)
           for i in  range(other):
            rot.append(compl((a**(1/other))*cos(((acos(self.r / a)*180/pi+(2*pi* i))/other)*pi/180) , (a ** (1/other)) * sin(((acos(self.r / a)*180/pi+(2*pi* i))/other)*pi/180)))
        return rot
    
    #module
    def abs(self):
        return sqrt(self.r ** 2 + self.i ** 2)
    
    
    def __repr__(self) -> str:
        return str(self.r) + " + " + str(self.i) + "i"
        