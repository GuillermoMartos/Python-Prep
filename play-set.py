import deck
import check_set

game_check=check_set.game_check

my_cards = [deck.Card(number, color, shape, shadow) for number in range(
    1, 4) for color in range(1, 4) for shape in range(1, 4) for shadow in range(1, 4)]
my_deck = deck.Deck(my_cards)
my_deck.mix()
# my_deck.__str__()
print("turn!")

table = []
for i in range(0, 6):
    table.append(my_deck.turn())


message=("starting table")
for card in table:
    print(card)
   
print("turn!")
import html_start
html_start=html_start.html_function
html_start(message, table, my_deck)

while len(my_deck.cards) >= 0:
    print(f"n° of cards deck remain: {len(my_deck.cards)}")
    available = table
    i = 1
    for card in available:
        print(f"{i}) {card}")
        i += 1
    choose1 = int(input(f"choose from 1 to {len(available)}: "))-1
    print(f" removed {available[choose1]}")
    card1 = available[choose1]
    available.remove(available[choose1])

    i = 1
    for card in available:
        print(f"{i}) {card}")
        i += 1
    choose2 = int(input(f"choose from 1 to {len(available)}: "))-1
    print(f" removed {available[choose2]}")
    card2 = available[choose2]
    available.remove(available[choose2])

    i = 1
    for card in available:
        print(f"{i}) {card}")
        i += 1
    choose3 = int(input(f"choose from 1 to {len(available)}: "))-1
    print(f" removed {available[choose3]}")
    card3 = available[choose3]
    available.remove(available[choose3])

    if game_check(card1, card2, card3, message, table, my_deck):
        print("Well done! Set!")
    else:
        print("No set, return cards")
