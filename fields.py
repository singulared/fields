from numbers import Number
from primes import prime as MP


def euclid_extended(a, b):
    if abs(b) > abs(a):
        (x, y, d) = euclid_extended(b, a)
        return (y, x, d)

    if abs(b) == 0:
        return (1, 0, a)

    x1, x2, y1, y2 = 0, 1, 1, 0
    while abs(b) > 0:
        q, r = divmod(a, b)
        x = x2 - q * x1
        y = y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y

    return (x2, y2, a)


class Field(Number):
    prime = MP

    def __init__(self, value, prime=None):
        if prime:
            self.prime = prime
        self.value = value % self.prime

    def __add__(self, operand):
        value = self.check_operand(operand)
        return Field(self.value + value, self.prime)

    def __radd__(self, operand):
        return self + operand

    def __mul__(self, operand):
        value = self.check_operand(operand)
        return Field(self.value * value, self.prime)

    def __rmul__(self, operand):
        return self * operand

    def __sub__(self, operand):
        value = self.check_operand(operand)
        return Field(self.value - value, self.prime)

    def __rsub__(self, operand):
        return -self + operand

    def __divmod__(self, divisor):
        value = self.check_operand(divisor)
        q, r = divmod(self.value, value)
        return (Field(q, self.prime), Field(r, self.prime))

    def __rdivmod__(self, operand):
        value = self.check_operand(operand)
        q, r = divmod(value, self.value)
        return (Field(q, self.prime), Field(r, self.prime))

    def __mod__(self, divisor):
        return self.__divmod__(divisor)[1]

    def __rmod__(self, operand):
        return (operand % self.value)

    def __abs__(self):
        return abs(self.value)

    def __neg__(self):
        return Field(-self.value)

    def __eq__(self, operand):
        return isinstance(operand, Field) and self.value == operand.value

    def __repr__(self):
        return '{} (mod {})'.format(self.value, self.prime)

    def check_operand(self, operand):
        if isinstance(operand, Field):
            return operand.value
        elif isinstance(operand, int):
            return operand
        else:
            return int(operand)

    def inverse(self):
        x, y, d = euclid_extended(self.value, self.prime)
        if d != 1:
            raise ValueError("Error: p is not prime in %s!" % (self))
        return Field(x, self.prime)
