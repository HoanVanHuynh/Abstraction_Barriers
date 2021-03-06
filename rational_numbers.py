def rational(n, d):
    """ Return the rational number with numerator n and denominator d."""

def numer(rat):
    """ Return the numerator of the rational number rat."""

def denom(rat):
    """ Return the denominator of the rational number rat."""

def mul_rational(rat1, rat2):
    """ Multiply rat1 and rat2 and return a new rational number."""
    return rational(numer(rat1) * numer(rat2), denom(rat1) * denom(rat2))        

# Implementing Rational Numbers
# There are many different ways we could choose to implement rational numbers

# One of the simplest is to use lists
from fractions import gcd # Greatest common divisor

# This is a constructor that allow us to construct new instances of the data type
def rational(n, d):
    divisor = gcd(n,d) # Reduce to lowest terms
    return [n//divisor, d//divisor]
# This is a selector that allow us to access the different parts of the data type
def numer(rat):
    return rat[0]
def denom(rat):
    return rat[1]