'''
    TODO: dynamic docs
    b = 1
    c = 2
    a = b + c # reactive addition
    b = 10 
    print(a) # 12 because a is reactive
'''

class ReactiveInt(object):

    """ Reactive integer: naive, lazy implementation """

    def __init__(self, n=0):
        self.n = n
        self.refs = []

    def add(self, other):
        self.refs.append(other)

    def update(self, n):
        self.n = n

    def _val(self):
        return sum(ref.n for ref in self.refs) # lazy

    def __str__(self):
        return str(self._val())

    def __repr__(self):
        return repr([ref.n for ref in self.refs])
        
def main():
    b = ReactiveInt(1)
    c = ReactiveInt(2)
    a = ReactiveInt()

    a.add(b)
    a.add(c)
    print(repr(a))
    print(a)

    b.update(10)
    print(repr(a))
    print(a)

    assert a._val() == 12 

if __name__ == "__main__":
    main()

# TODO:  <23-02-23, bitmole> #
# Pass observer into the ints
