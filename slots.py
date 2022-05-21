###############
##tragaperras##
###############

#refrescar pantalla

from msilib.schema import Error
from time import sleep
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
                \x1b[1;37;40m|\x1b[0m       \x1b[1;31;40m CHERRY    x0.80  \x1b[0m        \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|Reglas de juego:                 |\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;34;40m BELL      x4.00  \x1b[0m        \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|Ganas dinero si consigues una    |\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;36;40m LEMON     x2.40  \x1b[0m        \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|diagonal, una fila o una columna |\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;33;40m ORANGE    x1.60  \x1b[0m        \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|del mismo símbolo, sino pierdes  |\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;35;40m SEVEN     x5.00 \x1b[0m         \x1b[1;37;40m|\x1b[0m                    \x1b[1;32;40m|la apuesta                       |\x1b[0m
                \x1b[1;37;40m+---------------------------------+\x1b[0m                    \x1b[1;37;40m+---------------------------------+\x1b[0m
    ''')

def valores():
    print('''
                \x1b[1;37;40m+---------------------------------+\x1b[0m               
                \x1b[1;37;40m|\x1b[0m       \x1b[1;31;40m CHERRY    x0.80  \x1b[0m        \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;34;40m BELL      x4.00  \x1b[0m        \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;36;40m LEMON     x2.40  \x1b[0m        \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;33;40m ORANGE    x1.60  \x1b[0m        \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m|\x1b[0m       \x1b[1;35;40m SEVEN     x5.00 \x1b[0m         \x1b[1;37;40m|\x1b[0m
                \x1b[1;37;40m+---------------------------------+\x1b[0m                    
    ''')

#constantes
dinero_inicial=30.0
a=0
items=['CHERRY','BELL','LEMON','ORANGE','SEVEN']
items_emoji={'CHERRY':'🍒','BELL':'🔔','LEMON':'🍋','ORANGE':'🍊','SEVEN':'7️⃣ '}

#mensaje inicio
mensaje_ini()
print('''
        Bienvenido a la máquina tragaperras🎰,
        Empiezas con '''+str(dinero_inicial)+'''€
        ''')
tabla_valores()

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

def apuestas():
    global apuesta, dinero
    numero=False
    while numero==False:
        try:
            apuesta=float(input('''
            Dinero a apostar: '''))
            valid=False
            while valid==False:
                if apuesta>0 and dinero>=apuesta:
                    valid=True
                    return apuesta
                elif apuesta<=0:
                    print('---->Tienes que apostar algo')
                    apuesta=float(input('''
            Dinero a apostar: '''))
                elif apuesta>dinero:
                    print('---->La apuesta no puede ser mayor al dinero que tienes')
                    apuesta=float(input('''
            Dinero a apostar: '''))
            numero=True
        except ValueError:
            print('---->Error de input!!!')

def jugar():
    global dinero, slotUno, slotDos, slotTres, slotUnoA, slotDosA, slotTresA, slotUnoB, slotDosB, slotTresB
    continuar=preguntarJugador()
    if continuar==True:
        apuestas()
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
        valores()
        if puntuacion()=='Has perdido':
            print('''Has perdido''')
            playsound('./sonidos/bank.wav')
        else:
            playsound('./sonidos/bonk.wav')
        if dinero>0:
            print('''
            \x1b[1;32;42m DINERO: \x1b[0m''',str(round(dinero,2))+'€')
            continuar=preguntarJugador()
            if continuar==True:
                apuestas()
        os.system('cls')
    mensaje_ini()
    if dinero<=0:
        print('Ya no tienes dinero para seguir jugando :(')
        sleep(2)
    if continuar==False:
            playsound('./sonidos/bank.wav')
            print('''
            
                                                 ___       ___ 
                                                |__  \_/ |  |  
                                                |___ / \ |  |  
               

            ''')
            sleep(2)

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
    global dinero, slotUno, slotDos, slotTres, slotUnoA, slotDosA, slotTresA, slotUnoB, slotDosB, slotTresB, apuesta
    print('La apuesta es de',apuesta,'euros')
    #slots del medio
    if ((slotUno=='CHERRY') and (slotDos=='CHERRY') and (slotTres=='CHERRY')):
        win1=apuesta*0.80
    elif ((slotUno=='BELL') and (slotDos=='BELL') and (slotTres=='BELL')):
        win1=apuesta*4.00
    elif ((slotUno=='LEMON') and (slotDos=='LEMON') and (slotTres=='LEMON')):
        win1=apuesta*2.40
    elif ((slotUno=='ORANGE') and (slotDos=='ORANGE') and (slotTres=='ORANGE')):
        win1=apuesta*1.60
    elif ((slotUno=='SEVEN') and (slotDos=='SEVEN') and (slotTres=='SEVEN')):
        win1=apuesta*5.0
    else:
        win1=0
    dinero+=win1
    #slots arriba
    if ((slotUnoA=='CHERRY') and (slotDosA=='CHERRY') and (slotTresA=='CHERRY')):
        win2=apuesta*0.80
    elif ((slotUnoA=='BELL') and (slotDosA=='BELL') and (slotTresA=='BELL')):
        win2=apuesta*4.00
    elif ((slotUnoA=='LEMON') and (slotDosA=='LEMON') and (slotTresA=='LEMON')):
        win2=apuesta*2.40
    elif ((slotUnoA=='ORANGE') and (slotDosA=='ORANGE') and (slotTresA=='ORANGE')):
        win2=apuesta*1.60
    elif ((slotUnoA=='SEVEN') and (slotDosA=='SEVEN') and (slotTresA=='SEVEN')):
        win2=apuesta*5.00
    else:
        win2=0
    dinero+=win2
    #slots abajo
    if ((slotUnoB=='CHERRY') and (slotDosB=='CHERRY') and (slotTresB=='CHERRY')):
        win3=apuesta*0.80
    elif ((slotUnoB=='BELL') and (slotDosB=='BELL') and (slotTresB=='BELL')):
        win3=apuesta*4.00
    elif ((slotUnoB=='LEMON') and (slotDosB=='LEMON') and (slotTresB=='LEMON')):
        win3=apuesta*2.40
    elif ((slotUnoB=='ORANGE') and (slotDosB=='ORANGE') and (slotTresB=='ORANGE')):
        win3=apuesta*1.60
    elif ((slotUnoB=='SEVEN') and (slotDosB=='SEVEN') and (slotTresB=='SEVEN')):
        win3=apuesta*5.00
    else:
        win3=0
    dinero+=win3
    #diagonal \
    if ((slotUnoA=='CHERRY') and (slotDos=='CHERRY') and (slotTresB=='CHERRY')):
        win4=apuesta*0.80
    elif ((slotUnoA=='BELL') and (slotDos=='BELL') and (slotTresB=='BELL')):
        win4=apuesta*4.00
    elif ((slotUnoA=='LEMON') and (slotDos=='LEMON') and (slotTresB=='LEMON')):
        win4=apuesta*2.40
    elif ((slotUnoA=='ORANGE') and (slotDos=='ORANGE') and (slotTresB=='ORANGE')):
        win4=apuesta*1.60
    elif ((slotUnoA=='SEVEN') and (slotDos=='SEVEN') and (slotTresB=='SEVEN')):
        win4=apuesta*5.00
    else:
        win4=0
    dinero+=win4
    #diagonal /
    if ((slotUnoB=='CHERRY') and (slotDos=='CHERRY') and (slotTresA=='CHERRY')):
        win5=apuesta*0.80
    elif ((slotUnoB=='BELL') and (slotDos=='BELL') and (slotTresA=='BELL')):
        win5=apuesta*4.00
    elif ((slotUnoB =='LEMON') and (slotDos=='LEMON') and (slotTresA=='LEMON')):
        win5=apuesta*2.40
    elif ((slotUnoB=='ORANGE') and (slotDos=='ORANGE') and (slotTresA=='ORANGE')):
        win5=apuesta*1.60
    elif ((slotUnoB=='SEVEN') and (slotDos=='SEVEN') and (slotTresA=='SEVEN')):
        win5=apuesta*5.00
    else:
        win5=0
    dinero+=win5
    #slot 1
    if ((slotUnoA=='CHERRY') and (slotUno=='CHERRY') and (slotUnoB=='CHERRY')):
        win6=apuesta*0.80
    elif ((slotUnoA=='BELL') and (slotUno=='BELL') and (slotUnoB=='BELL')):
        win6=apuesta*4.00
    elif ((slotUnoA =='LEMON') and (slotUno=='LEMON') and (slotUnoB=='LEMON')):
        win6=apuesta*2.40
    elif ((slotUnoA=='ORANGE') and (slotUno=='ORANGE') and (slotUnoB=='ORANGE')):
        win6=apuesta*1.60
    elif ((slotUnoA=='SEVEN') and (slotUno=='SEVEN') and (slotUnoB=='SEVEN')):
        win6=apuesta*5.00
    else:
        win6=0
    dinero+=win6
    #slot 2
    if ((slotDosA=='CHERRY') and (slotDos=='CHERRY') and (slotDosB=='CHERRY')):
        win7=apuesta*0.80
    elif ((slotDosA=='BELL') and (slotDos=='BELL') and (slotDosB=='BELL')):
        win7=apuesta*4.00
    elif ((slotDosA =='LEMON') and (slotDos=='LEMON') and (slotDosB=='LEMON')):
        win7=apuesta*2.40
    elif ((slotDosA=='ORANGE') and (slotDos=='ORANGE') and (slotDosB=='ORANGE')):
        win7=apuesta*1.60
    elif ((slotDosA=='SEVEN') and (slotDos=='SEVEN') and (slotDosB=='SEVEN')):
        win7=apuesta*5.00
    else:
        win7=0
    dinero+=win7
    #slot 3
    if ((slotTresA=='CHERRY') and (slotTres=='CHERRY') and (slotTresB=='CHERRY')):
        win8=apuesta*0.80
    elif ((slotTresA=='BELL') and (slotTres=='BELL') and (slotTresB=='BELL')):
        win8=apuesta*4.00
    elif ((slotTresA =='LEMON') and (slotTres=='LEMON') and (slotTresB=='LEMON')):
        win8=apuesta*2.40
    elif ((slotTresA=='ORANGE') and (slotTres=='ORANGE') and (slotTresB=='ORANGE')):
        win8=apuesta*1.60
    elif ((slotTresA=='SEVEN') and (slotTres=='SEVEN') and (slotTresB=='SEVEN')):
        win8=apuesta*5.00
    else:
        win8=0
    dinero+=win8
    if (win1==0 and win2==0 and win3==0 and win4==0 and win5==0 and win6==0 and win7==0 and win8==0):
        dinero-=apuesta
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



