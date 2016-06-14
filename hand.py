from card import *

class Hand(object):
    def __init__(self):
        self.hand = []
        self.SoftValue = 0
        self.HardValue = 0
        self.busted = False
        self.blackjack = False

    def getHand(self,newHand):
        return self.hand

    def setSoftValue(self,newSoftValue):
        self.SoftValue=newSoftValue

    def getSoftValue(self):
        return self.SoftValue

    def setHardValue(self,newHardValue):
        self.hardValue=newHardValue

    def getHardValue(self):
        return self.HardValue

    def setBlackjack(self,blackjack):
        self.blackjack

    def getBlackjack(self):
        return self.blackjack

    def setBusted(self,busted):
        self.busted=busted

    def getBusted(self):
        return self.busted

    def getNumberOfCards(self):
        return len(self.hand)

    def getCardAtPosition(self, cardPosiion):
        if cardPosiion < len(self.hand):
            return self.hand[cardPosiion - 1]
        else:
            return None
    
    def addCard(self, newCard):
        self.hand.append(newCard)
        self.SoftValue += Card.SoftValue()
        self.HardValue += Card.HardValue()
        if self.SoftValue>21 and self.HardValue>21:
            self.busted = True
        if self.SoftValue == 21 and self.hand == 2:
            self.blackjack = True






