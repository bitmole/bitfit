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

    def __init__(self, val=0):
        self._val = val
        self._refs = [self]

    def add(self, *args):
        self._refs.extend(args)

    @property
    def val(self):
        return sum(ref._val for ref in self._refs)

    @val.setter
    def val(self, val):
        self._val = val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return '%d %s' % (self.val, repr([ref._val for ref in self._refs]))

class ObservableInt(object):

    """ Reactive integer: push implementation """

    def __init__(self):
        """TODO: to be defined. """

class CustomInt(int):

    """ Custom reactive integer """
        
        
def main():
    a = ReactiveInt(1)
    b = ReactiveInt(2)
    c = ReactiveInt(3)

    assert a.val == 1

    # TODO: refactor to a = b.add(c)
    a.add(b, c)
    assert a.val == 6 # sum([1, 2, 3])

    b.val = 4
    assert a.val == 8 # sum([1, 4, 3])

    c.val = 5
    assert a.val == 10 # sum([1, 4, 5]) 

if __name__ == "__main__":
    main()

# TODO:  <23-02-23, bitmole> #
# Pass observer into the ints
