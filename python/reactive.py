'''
https://en.wikipedia.org/wiki/Reactive_programming
b = 1
c = 2
a = b + c # reactive addition
b = 10 
print(a) # 12 because a is reactive
'''

class ReactiveInt(object):

    """ Reactive integer: naive, lazy implementation """

    def __init__(self, val=0, refs=[]):
        self._val = val
        self._refs = refs

    def add(self, other):
        return ReactiveInt(refs=[self, other])

    @property
    def val(self):
        return self._val + sum(ref._val for ref in self._refs)

    @val.setter
    def val(self, val):
        self._val = val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return '%d %s' % (self.val, repr([ref._val for ref in self._refs]))

class ObservableInt(object):

    """ Reactive integer: push implementation """

    def __init__(self, val=0, refs=[]):
        self._val = val
        self._refs = refs
        self._observer = None

        for ref in self._refs:
            ref._observer = self

    def add(self,  other):
        return ObservableInt(self._val + other._val, refs=[self, other])

    def notify(self):
        self.val = sum(ref._val for ref in self._refs)

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val
        if self._observer is not None:
            self._observer.notify()

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return '%d %s' % (self.val, repr([ref._val for ref in self._refs]))


class InheritedReactiveInt(int):

    """ Custom reactive integer """
        
        
def test_lazy():
    a = ReactiveInt(1)
    b = ReactiveInt(2)

    c = a.add(b)
    assert c.val == 3 # sum([1, 2])

    a.val = 4
    assert c.val == 6 # sum([4, 2])

    b.val = 5
    assert c.val == 9 # sum([4, 5]) 

def test_observer():
    a = ObservableInt(1)
    b = ObservableInt(2)

    c = a.add(b)
    assert c.val == 3

    a.val = 4
    assert c.val == 6

    b.val = 5
    assert c.val == 9

def main():
    test_lazy()
    test_observer()

if __name__ == "__main__":
    main()

# TODO:  <23-02-23, bitmole> #
# Pass observer into the ints
