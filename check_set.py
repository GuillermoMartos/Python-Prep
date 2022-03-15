from stringprep import c6_set
import html_start

html_start=html_start.html_function

def game_check(a, b, c, message, table, my_deck):
    """
    descript: take 3 cards, check for set valid, return boolean
    rule: A set consists of three cards satisfying all of these conditions:
    They all have the same number or have three different numbers.
    They all have the same shape or have three different shapes.
    They all have the same shading or have three different shadings.
    They all have the same color or have three different colors.
    """

    # They all have the same number or have three different numbers.
    if a.number == b.number == c.number:
        print("all number are equal :)")
        message="all number are equal :)"
        for i in range(0, 3):
            if len(my_deck.cards) > 0:
                table.append(my_deck.turn())
        html_start(message,table, my_deck)
        return True
    if a.number != b.number & a.number != c.number & c.number != b.number:
        print("all number are different :)")
        message="all number are different :)"
        for i in range(0, 3):
            if len(my_deck.cards) > 0:
                table.append(my_deck.turn())
        html_start(message,table, my_deck)
        return True

    # They all have the same shape or have three different shapes.
    if a.shape == b.shape & b.shape == c.shape:
        print("all shape are equal :)")
        message="all shape are equal :)"
        for i in range(0, 3):
            if len(my_deck.cards) > 0:
                table.append(my_deck.turn())
        html_start(message,table, my_deck)
        return True
    if a.shape != b.shape & a.shape != c.shape & c.shape != b.shape:
        print("all shape are different :)")
        message="all shape are different :)"
        for i in range(0, 3):
            if len(my_deck.cards) > 0:
                table.append(my_deck.turn())
        html_start(message,table, my_deck)
        return True

    # They all have the same shading or have three different shadings.
    if a.shadow == b.shadow & b.shadow == c.shadow:
        print("all shadow are equal :)")
        message="all shadow are equal :)"
        for i in range(0, 3):
            if len(my_deck.cards) > 0:
                table.append(my_deck.turn())
        html_start(message,table, my_deck)
        return True
    if a.shadow != b.shadow & a.shadow != c.shadow & c.shadow != b.shadow:
        print("all shadow are different :)")
        message="all shadow are different :)"
        for i in range(0, 3):
            if len(my_deck.cards) > 0:
                table.append(my_deck.turn())
                
        html_start(message,table, my_deck)
        return True

    # They all have the same color or have three different colors.
    if a.color == b.color & b.color == c.color:
        print("all color are equal :)")
        message="all color are equal :)"
        for i in range(0, 3):
            if len(my_deck.cards) > 0:
                table.append(my_deck.turn())
        html_start(message,table, my_deck)
        return True
    if a.color != b.color & a.color != c.color & c.color != b.color:
        message="all color are different :)"
        print("all color are different :)")
        for i in range(0, 3):
            if len(my_deck.cards) > 0:
                table.append(my_deck.turn())
        html_start(message,table, my_deck)
        return True

    table.append(a)
    table.append(b)
    table.append(c)
    message="no set in combination :("
    html_start(message,table, my_deck)

    return False
