import random

class Card:
    """
    class card doc string......
    """
    def __init__(self, shape, num, color, shadow):
        self.shape=shape
        self.number=num
        self.color =color
        self.shadow=shadow
    def __str__(self):
        return f"Card (shape= {self.shape} ,color= {self.color}, num={self.number}, shadow={self.shadow} )"

class Deck:
    """
    class deck doc string......methods...
    """
    def __init__(self,cards):
        self.cards=cards
    def __str__(self):
        for card in self.cards:
            print(card)
    def mix(self):
        random.shuffle(self.cards)
    def turn(self):
        return self.cards.pop()
    
        

