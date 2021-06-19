"""
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')
"""
import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])
hs_card = collections.namedtuple('card', ['life', 'cost'])

class FrenchDeck:
    """ len
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    >>> deck[0]
    Card(rank='2', suit='spades')
    >>> deck[-1]
    Card(rank='A', suit='hearts')
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    """
    >>> 2+2
    4
    """
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    
    def __len__(self):
        return len(self._cards)
    
    
    def __getitem__(self, position):
        return self._cards[position]
    
    


class HSDeck:
    """ len
    >>> deck = HSDeck()
    >>> len(deck)
    121
    """
    lifes = [str(n) for n in range(0, 11)]
    costs = [str(n) for n in range(0, 11)]
    
    def __init__(self):
        self._cards = [hs_card(life, cost) for life in self.lifes
                                           for cost in self.costs]
    
    def __len__(self):
        return len(self._cards)
    
    
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    import doctest
    print('T!')
    doctest.testmod()