ROMAN_NUMERAL_MAP = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

    
class OutOfRangeError(ValueError): pass
class NonIntegerError(ValueError): pass

def to_roman(n):
    """Creates Roman representation of a given number

    :n: integer from 1 to 3999
    :returns: Roman numeral representation as a string

    """
    if not isinstance(n, int):
        raise NonIntegerError('non-integers cannot be converted')

    if not (0 < n < 4000):
        raise OutOfRangeError('number out of range (must be 1..4000)')

    result = ''
    for numeral, integer in ROMAN_NUMERAL_MAP:
        while n >= integer:
            result += numeral
            n -= integer
            # print(f'subtracting {integer} from input, adding {numeral} to output')
    return result

def from_roman(s):
    """Converts Roman numeral representation to integer

    :s: Roman numeral representation as a string
    :returns: integer

    """

    result = 0
    for numeral, integer in ROMAN_NUMERAL_MAP:
        while s.startswith(numeral):
            result += integer
            s = s[len(numeral):]

    return result
