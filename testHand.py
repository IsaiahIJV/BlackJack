from hand import *
from deck import *

testHand = Hand()
testDeck = Deck()
testCard = Card(rank=0, suit=0)
testDeck.shuffle()
testHand.addCard(testDeck.getTopCard())
for card in range(1, testHand.getNumberOfCards()):
    print(str(testHand.getCardAtPosition(card)))

testHand.addCard(testDeck.getTopCard())
testHand.addCard(testDeck.getTopCard())
for card in range(1, testHand.getNumberOfCards()):
    print(str(testHand.getCardAtPosition(card)))







