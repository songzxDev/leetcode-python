# -*- coding: utf-8 -*-
# @Time    : 2020-01-20 10:30
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : testcollections.py
# @Software: PyCharm

from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = tuple([str(n) for n in range(2, 11)] + list('JQKA'))
    suits = ('spades', 'diamonds', 'clubs', 'hearts',)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':
    french_deck = FrenchDeck()
    print french_deck[0]
    print french_deck[0].rank
    print french_deck[0].suit
