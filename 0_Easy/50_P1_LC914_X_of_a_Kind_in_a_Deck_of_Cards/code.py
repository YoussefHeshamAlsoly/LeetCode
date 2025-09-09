from collections import Counter
from math import gcd

def hasGroupsSizeX(deck:list):
    """
    :type deck: List[int]
    :rtype: bool
    """
    deck = Counter(deck)
    minimum_group_length = gcd(*deck.values())

    if minimum_group_length == 1:
        return False

    for i in deck.values():
        if i%minimum_group_length != 0:
            return False
    return True

deck = [1,1,1,2,2,2,3,3]
print(hasGroupsSizeX(deck))

