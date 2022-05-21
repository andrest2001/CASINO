###############
##tragaperras##
###############

#refrescar pantalla

import random
import os
from playsound import playsound

def mensaje_ini():
    print('''
     __   __  _______  _______  __   __  ___   __    _  _______    _______  ______    _______  _______  _______  _______  _______  ______    ______    _______  _______ 
    |  |_|  ||   _   ||       ||  | |  ||   | |  |  | ||   _   |  |       ||    _ |  |   _   ||       ||   _   ||       ||       ||    _ |  |    _ |  |   _   ||       |
    |       ||  |_|  ||   _   ||  | |  ||   | |   |_| ||  |_|  |  |_     _||   | ||  |  |_|  ||    ___||  |_|  ||    _  ||    ___||   | ||  |   | ||  |  |_|  ||  _____|
    |       ||       ||  | |  ||  |_|  ||   | |       ||       |    |   |  |   |_||_ |       ||   | __ |       ||   |_| ||   |___ |   |_||_ |   |_||_ |       || |_____ 
    |       ||       ||  |_|  ||       ||   | |  _    ||       |    |   |  |    __  ||       ||   ||  ||       ||    ___||    ___||    __  ||    __  ||       ||_____  |
    | ||_|| ||   _   ||      | |       ||   | | | |   ||   _   |    |   |  |   |  | ||   _   ||   |_| ||   _   ||   |    |   |___ |   |  | ||   |  | ||   _   | _____| |
    |_|   |_||__| |__||____||_||_______||___| |_|  |__||__| |__|    |___|  |___|  |_||__| |__||_______||__| |__||___|    |_______||___|  |_||___|  |_||__| |__||_______|
    ''')

#mensaje inicio
def tabla_valores():
    print('''
                \x1b[1;37;40m+---------------------------------+\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;31;40m CHERRY    -->0.80€ \x1b[0m      \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;34;40m BELL      -->4.00€ \x1b[0m      \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;36;40m LEMON     -->2.40€ \x1b[0m      \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;33;40m ORANGE    -->1.60€ \x1b[0m      \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;35;40m SEVEN     -->20.00€\x1b[0m      \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m+---------------------------------+\x1b[0m
    ''')
mensaje_ini()
print('''
        Bienvenido a la máquina tragaperras🎰,
        Empiezas con 30€
        ''')
tabla_valores()
#constantes
dinero_inicial=30.0
items=['CHERRY','BELL','LEMON','ORANGE','SEVEN']
items_emoji={'CHERRY':'🍒','BELL':'🔔','LEMON':'🍋','ORANGE':'🍊','SEVEN':'7️⃣ '}

#variabes
slotUno=None
slotDos=None
slotTres=None
dinero=dinero_inicial

def jugar():
    global dinero, slotUno, slotDos, slotTres
    continuar=preguntarJugador()
    os.system('cls')
    while (dinero>0 and continuar ==True):
        slotUno=tirada()
        slotDos=tirada()
        slotTres=tirada()
        mensaje_ini()
        print('''
                         \x1b[0;30;47m|          |\x1b[0m
                      \x1b[0;30;47m|                |\x1b[0m
                    \x1b[0;30;47m|      \x1b[1;33;40m CASINO \x1b[0;30;47m      |\x1b[0m
                    \x1b[1;37;47m|____________________|\x1b[0m
                    \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m
                \x1b[1;32;42m ++\x1b[0m \x1b[1;37;47m|\x1b[0m ''',items_emoji[items[random.randrange(0,5)]],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[items[random.randrange(0,5)]],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[items[random.randrange(0,5)]],''' \x1b[1;37;47m|\x1b[0m
                \x1b[1;32;42m ||\x1b[0m \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m
                \x1b[1;32;42m -> \x1b[0m\x1b[1;37;47m|\x1b[0m ''',items_emoji[slotUno],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotDos],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotTres],''' \x1b[1;37;47m|\x1b[0m 
                    \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m
                    \x1b[1;37;47m|\x1b[0m ''',items_emoji[items[random.randrange(0,5)]],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[items[random.randrange(0,5)]],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[items[random.randrange(0,5)]],''' \x1b[1;37;47m|\x1b[0m
                    \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m
                    \x1b[1;37;47m|____________________|\x1b[0m
                    \x1b[7;37;40m|<><><><><><><><><><>|\x1b[0m
                    \x1b[7;37;40m|<><><><><><><><><><>|\x1b[0m
                    \x1b[7;37;40m|<><><><><><><><><><>|\x1b[0m
                    \x1b[1;37;47m|____________________|\x1b[0m
                    \x1b[2;37;44m|<><><><><><><><><><>|\x1b[0m
                    ''')
        puntuacion()
        if dinero>0:
            print('''
            \x1b[1;32;42m DINERO: \x1b[0m''',str(round(dinero,2))+'€')
            continuar=preguntarJugador()
        os.system('cls')
    mensaje_ini()
    if dinero<=0:
        print('Ya no tienes dinero para seguir jugando :(')
    if continuar==False:
            print('EXIT')

def preguntarJugador():
    global dinero
    pregunta=input('''
Tirar? s/n: ''').lower()
    while pregunta!='s' or pregunta!='n':
        if pregunta=='s':
            return True
        elif pregunta=='n':
            return False
        else:
            print('---->Input erróneo. Volver a intentar')
            pregunta=input('''
Tirar? s/n: ''')

def tirada():
    #devuelve un item aleatorio
    aleatorio=random.randint(0,4)
    return items[aleatorio]

def puntuacion():
    global dinero, slotUno, slotDos, slotTres

    if ((slotUno=='CHERRY') and (slotDos=='CHERRY') and (slotTres=='CHERRY')):
        win=0.80
    elif ((slotUno=='BELL') and (slotDos=='BELL') and (slotTres=='BELL')):
        win=4.0
    elif ((slotUno=='LEMON') and (slotDos=='LEMON') and (slotTres=='LEMON')):
        win=2.4
    elif ((slotUno=='ORANGE') and (slotDos=='ORANGE') and (slotTres=='ORANGE')):
        win=1.6
    elif ((slotUno=='SEVEN') and (slotDos=='SEVEN') and (slotTres=='SEVEN')):
        win=20.0
    else:
        win=-1.0
    dinero+=win
    if win>0:
        print('---->Has ganado',str(win)+'€')
    else:
        print('''
        Has perdido''')

jugar()


