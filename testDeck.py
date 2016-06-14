from deck import *

aDeck = Deck()

for cardNumber in range(0, 10):
    print(aDeck.getTopCard())

aDeck.shuffle()

for cardNumber in range(0, 10):
    print(aDeck.getTopCard())

