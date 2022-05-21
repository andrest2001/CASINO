###############
##tragaperras##
###############

#refrescar pantalla

from winsound import PlaySound
from playsound import playsound
import random
import os

def mensaje_ini():
    print('''
    \x1b[0;37;40m
                                                                                                                                                            
    ███    ███  █████   ██████  ██    ██ ██ ███    ██  █████      ████████ ██████   █████   ██████   █████  ██████  ███████ ██████  ██████   █████  ███████ 
    ████  ████ ██   ██ ██    ██ ██    ██ ██ ████   ██ ██   ██        ██    ██   ██ ██   ██ ██       ██   ██ ██   ██ ██      ██   ██ ██   ██ ██   ██ ██      
    ██ ████ ██ ███████ ██    ██ ██    ██ ██ ██ ██  ██ ███████        ██    ██████  ███████ ██   ███ ███████ ██████  █████   ██████  ██████  ███████ ███████ 
    ██  ██  ██ ██   ██ ██ ▄▄ ██ ██    ██ ██ ██  ██ ██ ██   ██        ██    ██   ██ ██   ██ ██    ██ ██   ██ ██      ██      ██   ██ ██   ██ ██   ██      ██ 
    ██      ██ ██   ██  ██████   ██████  ██ ██   ████ ██   ██        ██    ██   ██ ██   ██  ██████  ██   ██ ██      ███████ ██   ██ ██   ██ ██   ██ ███████ 
                       ▀▀                                                                                                                                   \x1b[0m''')

def tabla_valores():
    print('''
                \x1b[1;37;40m+---------------------------------+\x1b[0m                    \x1b[1;37;40m+---------------------------------+\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;31;40m CHERRY    -->0.80€ \x1b[0m      \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|Reglas de juego:                 |\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;34;40m BELL      -->4.00€ \x1b[0m      \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|Ganas dinero si consigues una    |\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;36;40m LEMON     -->2.40€ \x1b[0m      \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|diagonal, una fila o una columna |\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;33;40m ORANGE    -->1.60€ \x1b[0m      \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|del mismo símbolo, sino pierdes  |\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;35;40m SEVEN     -->20.00€\x1b[0m      \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|un euro                          |\x1b[0m
                \x1b[1;37;40m+---------------------------------+\x1b[0m                    \x1b[1;37;40m+---------------------------------+\x1b[0m
    ''')
#mensaje inicio
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
slotUnoA=None
slotDosA=None
slotTresA=None
slotUnoB=None
slotDosB=None
slotTresB=None
dinero=dinero_inicial

def jugar():
    global dinero, slotUno, slotDos, slotTres, slotUnoA, slotDosA, slotTresA, slotUnoB, slotDosB, slotTresB
    continuar=preguntarJugador()
    os.system('cls')
    while (dinero>0 and continuar ==True):
        slotUno=tirada()
        slotDos=tirada()
        slotTres=tirada()
        slotUnoA=tirada()
        slotDosA=tirada()
        slotTresA=tirada()
        slotUnoB=tirada()
        slotDosB=tirada()
        slotTresB=tirada()
        mensaje_ini()
        print('''
                         \x1b[0;30;47m|          |\x1b[0m
                      \x1b[0;30;47m|                |\x1b[0m
                    \x1b[0;30;47m|      \x1b[1;33;40m CASINO \x1b[0;30;47m      |\x1b[0m
                    \x1b[1;37;47m|____________________|\x1b[0m
                    \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m
                \x1b[1;32;42m ++\x1b[0m \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotUnoA],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotDosA],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotTresA],''' \x1b[1;37;47m|\x1b[0m
                \x1b[1;32;42m ||\x1b[0m \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m
                \x1b[1;32;42m -> \x1b[0m\x1b[1;37;47m|\x1b[0m ''',items_emoji[slotUno],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotDos],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotTres],''' \x1b[1;37;47m|\x1b[0m 
                    \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m
                    \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotUnoB],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotDosB],''' \x1b[1;37;47m|\x1b[0m ''',items_emoji[slotTresB],''' \x1b[1;37;47m|\x1b[0m
                    \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m      \x1b[1;37;47m|\x1b[0m
                    \x1b[1;37;47m|____________________|\x1b[0m
                    \x1b[7;37;40m|<><><><><><><><><><>|\x1b[0m
                    \x1b[7;37;40m|<><><><><><><><><><>|\x1b[0m
                    \x1b[7;37;40m|<><><><><><><><><><>|\x1b[0m
                    \x1b[1;37;47m|____________________|\x1b[0m
                    \x1b[2;37;44m|<><><><><><><><><><>|\x1b[0m
                    ''')
        if puntuacion()=='Has perdido':
            print('''Has perdido''')
            playsound('./sonidos/bank.wav')
        else:
            playsound('./sonidos/bonk.wav')
        if dinero>0:
            print('''
            \x1b[1;32;42m DINERO: \x1b[0m''',str(round(dinero,2))+'€')
            continuar=preguntarJugador()
        os.system('cls')
    mensaje_ini()
    if dinero<=0:
        print('Ya no tienes dinero para seguir jugando :(')
    if continuar==False:
            playsound('./sonidos/bank.wav')
            print('''
            
                                                 ___       ___ 
                                                |__  \_/ |  |  
                                                |___ / \ |  |  
               

            ''')

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
    global dinero, slotUno, slotDos, slotTres, slotUnoA, slotDosA, slotTresA, slotUnoB, slotDosB, slotTresB
    #slots del medio
    if ((slotUno=='CHERRY') and (slotDos=='CHERRY') and (slotTres=='CHERRY')):
        win1=0.80
    elif ((slotUno=='BELL') and (slotDos=='BELL') and (slotTres=='BELL')):
        win1=4.00
    elif ((slotUno=='LEMON') and (slotDos=='LEMON') and (slotTres=='LEMON')):
        win1=2.40
    elif ((slotUno=='ORANGE') and (slotDos=='ORANGE') and (slotTres=='ORANGE')):
        win1=1.60
    elif ((slotUno=='SEVEN') and (slotDos=='SEVEN') and (slotTres=='SEVEN')):
        win1=20.00
    else:
        win1=0
    dinero+=win1
    #slots arriba
    if ((slotUnoA=='CHERRY') and (slotDosA=='CHERRY') and (slotTresA=='CHERRY')):
        win2=0.80
    elif ((slotUnoA=='BELL') and (slotDosA=='BELL') and (slotTresA=='BELL')):
        win2=4.00
    elif ((slotUnoA=='LEMON') and (slotDosA=='LEMON') and (slotTresA=='LEMON')):
        win2=2.40
    elif ((slotUnoA=='ORANGE') and (slotDosA=='ORANGE') and (slotTresA=='ORANGE')):
        win2=1.60
    elif ((slotUnoA=='SEVEN') and (slotDosA=='SEVEN') and (slotTresA=='SEVEN')):
        win2=20.00
    else:
        win2=0
    dinero+=win2
    #slots abajo
    if ((slotUnoB=='CHERRY') and (slotDosB=='CHERRY') and (slotTresB=='CHERRY')):
        win3=0.80
    elif ((slotUnoB=='BELL') and (slotDosB=='BELL') and (slotTresB=='BELL')):
        win3=4.00
    elif ((slotUnoB=='LEMON') and (slotDosB=='LEMON') and (slotTresB=='LEMON')):
        win3=2.40
    elif ((slotUnoB=='ORANGE') and (slotDosB=='ORANGE') and (slotTresB=='ORANGE')):
        win3=1.60
    elif ((slotUnoB=='SEVEN') and (slotDosB=='SEVEN') and (slotTresB=='SEVEN')):
        win3=20.00
    else:
        win3=0
    dinero+=win3
    #diagonal \
    if ((slotUnoA=='CHERRY') and (slotDos=='CHERRY') and (slotTresB=='CHERRY')):
        win4=0.80
    elif ((slotUnoA=='BELL') and (slotDos=='BELL') and (slotTresB=='BELL')):
        win4=4.00
    elif ((slotUnoA=='LEMON') and (slotDos=='LEMON') and (slotTresB=='LEMON')):
        win4=2.40
    elif ((slotUnoA=='ORANGE') and (slotDos=='ORANGE') and (slotTresB=='ORANGE')):
        win4=1.60
    elif ((slotUnoA=='SEVEN') and (slotDos=='SEVEN') and (slotTresB=='SEVEN')):
        win4=20.00
    else:
        win4=0
    dinero+=win4
    #diagonal /
    if ((slotUnoB=='CHERRY') and (slotDos=='CHERRY') and (slotTresA=='CHERRY')):
        win5=0.80
    elif ((slotUnoB=='BELL') and (slotDos=='BELL') and (slotTresA=='BELL')):
        win5=4.00
    elif ((slotUnoB =='LEMON') and (slotDos=='LEMON') and (slotTresA=='LEMON')):
        win5=2.40
    elif ((slotUnoB=='ORANGE') and (slotDos=='ORANGE') and (slotTresA=='ORANGE')):
        win5=1.60
    elif ((slotUnoB=='SEVEN') and (slotDos=='SEVEN') and (slotTresA=='SEVEN')):
        win5=20.00
    else:
        win5=0
    dinero+=win5
    #slot 1
    if ((slotUnoA=='CHERRY') and (slotUno=='CHERRY') and (slotUnoB=='CHERRY')):
        win6=0.80
    elif ((slotUnoA=='BELL') and (slotUno=='BELL') and (slotUnoB=='BELL')):
        win6=4.00
    elif ((slotUnoA =='LEMON') and (slotUno=='LEMON') and (slotUnoB=='LEMON')):
        win6=2.40
    elif ((slotUnoA=='ORANGE') and (slotUno=='ORANGE') and (slotUnoB=='ORANGE')):
        win6=1.60
    elif ((slotUnoA=='SEVEN') and (slotUno=='SEVEN') and (slotUnoB=='SEVEN')):
        win6=20.00
    else:
        win6=0
    dinero+=win6
    #slot 2
    if ((slotDosA=='CHERRY') and (slotDos=='CHERRY') and (slotDosB=='CHERRY')):
        win7=0.80
    elif ((slotDosA=='BELL') and (slotDos=='BELL') and (slotDosB=='BELL')):
        win7=4.00
    elif ((slotDosA =='LEMON') and (slotDos=='LEMON') and (slotDosB=='LEMON')):
        win7=2.40
    elif ((slotDosA=='ORANGE') and (slotDos=='ORANGE') and (slotDosB=='ORANGE')):
        win7=1.60
    elif ((slotDosA=='SEVEN') and (slotDos=='SEVEN') and (slotDosB=='SEVEN')):
        win7=20.00
    else:
        win7=0
    dinero+=win7
    #slot 3
    if ((slotTresA=='CHERRY') and (slotTres=='CHERRY') and (slotTresB=='CHERRY')):
        win8=0.80
    elif ((slotTresA=='BELL') and (slotTres=='BELL') and (slotTresB=='BELL')):
        win8=4.00
    elif ((slotTresA =='LEMON') and (slotTres=='LEMON') and (slotTresB=='LEMON')):
        win8=2.40
    elif ((slotTresA=='ORANGE') and (slotTres=='ORANGE') and (slotTresB=='ORANGE')):
        win8=1.60
    elif ((slotTresA=='SEVEN') and (slotTres=='SEVEN') and (slotTresB=='SEVEN')):
        win8=20.00
    else:
        win8=0
    dinero+=win8
    if (win1==0 and win2==0 and win3==0 and win4==0 and win5==0 and win6==0 and win7==0 and win8==0):
        dinero-=1.00
    if win1>0:
        print('---->Has ganado',str(round(win1,2))+'€')
    if win2>0:
        print('---->Has ganado',str(round(win2,2))+'€')
    if win3>0:
        print('---->Has ganado',str(round(win3,2))+'€')
    if win4>0:
        print('---->Has ganado',str(round(win4,2))+'€')
    if win5>0:
        print('---->Has ganado',str(round(win5,2))+'€')
    if win6>0:
        print('---->Has ganado',str(round(win6,2))+'€')
    if win7>0:
        print('---->Has ganado',str(round(win7,2))+'€')
    if win8>0:
        print('---->Has ganado',str(round(win8,2))+'€')
    elif(win1==0 and win2==0 and win3==0 and win4==0 and win5==0 and win6==0 and win7==0 and win8==0):
        return 'Has perdido'

playsound('./sonidos/start_sound.wav')
jugar()



