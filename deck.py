from card import *
from random import shuffle

class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in ['C','S','H','D']:
            for rank in range (1,14):
                if rank >=2 and 1<= 11:
                    self.deck.append(Card(rank, suit))
                elif rank >= 11 and rank <=13:
                    self.deck.append(Face(rank,suit))
                elif rank ==1:
                    self.deck.append(Face(rank,suit))
                else:
                    print("Error Unknown Rank")

            self.numberOFCards = len(self.deck)


    def shuffle(self):
        shuffle(self.deck)
        return

    def getTopCard(self):
        tempCard=self.deck.pop()
        self.numberOFCards-=1
        return tempCard

