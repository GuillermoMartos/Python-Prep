from tabnanny import check
import deck
my_cards =[deck.Card(number, color, shape,shadow) for number in range(1, 4) for color in range(1, 4) for shape in range(1, 4) for shadow in range(1, 4)]
my_deck=deck.Deck(my_cards)

my_deck.mix()
# my_deck.__str__()
print("turn!")

table=[]
for i in range(0,6): 
    table.append(my_deck.turn())


def game_check(a,b,c):
    """
    descript: take 3 cards, check for set valid, return boolean
    rule: A set consists of three cards satisfying all of these conditions:
    They all have the same number or have three different numbers.
    They all have the same shape or have three different shapes.
    They all have the same shading or have three different shadings.
    They all have the same color or have three different colors.
    """
    
    #They all have the same number or have three different numbers.
    if a.number==b.number==c.number:
        print("all number are equal :)")
        for i in range(0,3):
            if len(my_deck.cards)>0:
                table.append(my_deck.turn())
        return True
    if a.number!=b.number & a.number!=c.number & c.number!=b.number:
        print(card1)
        print("all number are different :)")
        for i in range(0,3):
            if len(my_deck.cards)>0:
                table.append(my_deck.turn())
        return True
    
    # They all have the same shape or have three different shapes.
    if a.shape==b.shape & b.shape==c.shape:
        print("all shape are equal :)")
        for i in range(0,3):
            if len(my_deck.cards)>0:
                table.append(my_deck.turn())
        return True
    if a.shape!=b.shape & a.shape!=c.shape & c.shape!=b.shape:
        print("all shape are different :)")
        for i in range(0,3):
            if len(my_deck.cards)>0:
                table.append(my_deck.turn())
        return True
    
    # They all have the same shading or have three different shadings.
    if a.shadow==b.shadow & b.shadow==c.shadow:
        print("all shadow are equal :)")
        for i in range(0,3):
            if len(my_deck.cards)>0:
                table.append(my_deck.turn())
        return True
    if a.shadow!=b.shadow & a.shadow!=c.shadow & c.shadow!=b.shadow:
        print("all shadow are different :)")
        for i in range(0,3):
            if len(my_deck.cards)>0:
                table.append(my_deck.turn())
        return True
    
    # They all have the same color or have three different colors.
    if a.color==b.color & b.color==c.color:
        print("all color are equal :)")
        for i in range(0,3):
            if len(my_deck.cards)>0:
                table.append(my_deck.turn())
        return True
    if a.color!=b.color & a.color!=c.color & c.color!=b.color:
        print("all color are different :)")
        for i in range(0,3):
            if len(my_deck.cards)>0:
                table.append(my_deck.turn())
        return True   

    table.append(card1)
    table.append(card2)
    table.append(card3)

    
    return False
    

print("starting table")
for card in table:
    print(card)    


print("turn!")

while len(my_deck.cards)>=0:
    print(f"n° of cards deck remain: {len(my_deck.cards)}")
    available=table
    i=1
    for card in available :
        print(f"{i}) {card}")
        i+=1
    choose1=int(input(f"choose from 1 to {len(available)}: " ))-1
    print(f" removed {available[choose1]}")
    card1=available[choose1]
    available.remove(available[choose1])
    
    i=1
    for card in available :
        print(f"{i}) {card}")
        i+=1
    choose2=int(input(f"choose from 1 to {len(available)}: " ))-1
    print(f" removed {available[choose2]}")
    card2=available[choose2]
    available.remove(available[choose2])
    
    i=1
    for card in available :
        print(f"{i}) {card}")
        i+=1
    choose3=int(input(f"choose from 1 to {len(available)}: " ))-1
    print(f" removed {available[choose3]}")
    card3=available[choose3]
    available.remove(available[choose3])
   
    if game_check(card1, card2, card3):
        print("Well done! Set!")
    else:
        print("No set, return cards")
