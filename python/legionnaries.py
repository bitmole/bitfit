'''
Legionnaries
In the range 1 - 13 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13) the digit 1
occurs 6 times.

In the range, 1 - 2,660 (half the number of Romans in a legion), expressed in
Roman numerals, how many times does the numeral “X” occur?
'''

from romans import to_roman

def x_count(n):
    return sum(to_roman(i).count('X') for i in range(1, n+1))

if __name__ == "__main__":
    HALF_LEGION = 2660
    assert(x_count(HALF_LEGION) == 3977)
