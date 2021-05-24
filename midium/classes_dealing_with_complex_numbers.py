class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        return complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    def __truediv__(self, other):
        try: 
            return self.__mul__(complex(other.real, -1 * other.imag)).__mul__(complex(1.0/(other.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None
    def mod(self):
        return complex(((self.real**2+self.imag**2) ** 0.5), 0)
    def __str__(self):
        return str(round(self.real, 2))+('+' if self.imag>=0 else '-') + str(round(abs(self.imag), 2))+'i'
   

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')