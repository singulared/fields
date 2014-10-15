from primes import prime as MP
from numbers import Number


class Field(Number):
    prime = MP

    def __init__(self, value, prime=None):
        if prime:
            self.prime = prime
        self.value = value % self.prime

    def check_operand(self, operand):
        if isinstance(operand, Field):
            return operand.value
        elif isinstance(operand, int):
            return operand
        else:
            return int(operand)

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

    def __abs__(self):
        return abs(self.value)

    def __neg__(self):
        return Field(-self.value)

    def __eq__(self, operand):
        return isinstance(operand, Field) and self.value == operand.value

    def __repr__(self):
        return '{} (mod {})'.format(self.value, self.prime)
