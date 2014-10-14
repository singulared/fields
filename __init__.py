from .primes import prime as MP


class Integer:
    prime = MP

    def __init__(self, value, prime=None):
        if prime:
            self.prime = prime
        self.value = value % self.prime

    def __add__(self, operand):
        if isinstance(operand, Integer):
            value = operand.value
        else:
            value = operand
        return Integer(self.value + value, self.prime)

    def __radd__(self, operand):
        return self + operand

    def __repr__(self):
        return '{} (mod {})'.format(self.value, self.prime)
