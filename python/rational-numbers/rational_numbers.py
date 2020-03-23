from math import gcd

class Rational:
    def __init__(self, numer, denom):
        if numer == 0:      denom = 1
        elif denom < 0:     numer, denom = -numer,-denom
        gcd_v = gcd(numer, denom)
        self.numer = numer // gcd_v
        self.denom = denom // gcd_v

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer,
        self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom,
        self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer,
        self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom,
        self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer),
        abs(self.denom))

    def __pow__(self, power):
        if type(pow) is float:
            return (self.numer ** power) / (self.denom ** power)
        elif power > -1:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(self.numer ** abs(power), self.denom ** abs(power))

    def __rpow__(self, base):
        return base ** (self.numer/self.denom)