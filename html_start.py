import webbrowser
def html_function(message, table, my_deck):
    

    f = open('play.html', 'w')

    mensaje = """<html>
    <head></head>
    <body>
    <h1>%s</h1>
    <div>CARDS FOR SET</div>

    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>



    <div>DECK SET</div>
    <h1>%s</h1>

    </body>
    </html>""" % (message, table[0], table[1], table[2], table[3], table[4], table[5], len(my_deck.cards))

    f.write(mensaje)
    f.close()
    webbrowser.open_new_tab('play.html')