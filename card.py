Clubs="C"
Diamond="D"
Hearts="H"
Spades="S"
class Card (object):
    def __init__(self,rank,suit):
        self.suit=suit
        self.SoftValue=rank
        self.HardValue=rank
        self.rank=rank

    def __str__(self):
        return str(self.rank) + " of " + self.suit
    
    def setsuit(self,newSuit):
        self.suit=newSuit

    def getsuit(self):
        return self.suit

    def setSoftValue(self,newSoftValue):
        self.SoftValue=newSoftValue

    def getSoftValue(self):
        return self.SoftValue

    def setHardValue(self,newHardValue):
        self.HardValue=newHardValue

    def getHardValue(self):
        return self.HardValue

    def setRank(self,Rank):
        self.rank=Rank

    def getrank(self):
        return self.rank
    
class Face(Card):
    def __init__(self, rank, suit):
        super().__init__(rank, suit)
        self.SoftValue = self.HardValue = 10
        
class Ace(Card):
    def __init__(self,rank,suit):
        super().__init__(rank, suit)
        self.SoftValue=11
        self.HardValue=1


card1=Card(2, 'Hearts')
print("card1")
print(card1)
print(card1.getsuit())
print(card1.getrank())
print(card1)