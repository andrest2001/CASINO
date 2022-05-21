import random
import os
import time
 
class Carta:
    def __init__(self, suit, value, carta_value):
         
       
        self.suit = suit
 
 
        self.value = value
 
 
        self.carta_value = carta_value
 
def clear():
    os.system("clear")
 
def print_cartas(cartas, hidden):
         
    s = ""
    for carta in cartas:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for carta in cartas:
        if carta.value == '10':
            s = s + "\t|  {}            |".format(carta.value)
        else:
            s = s + "\t|  {}             |".format(carta.value)  
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for carta in cartas:
        s = s + "\t|       {}        |".format(carta.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
 
    s = ""
    for carta in cartas:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for carta in cartas:
        if carta.value == '10':
            s = s + "\t|            {}  |".format(carta.value)
        else:
            s = s + "\t|            {}   |".format(carta.value)
    if hidden:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for carta in cartas:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()


 
 
def blackjack_game(deck):

    banco = 2000
    jugador_cartas = []
    crupier_cartas = []
 
    jugador_puntuacion = 0
    crupier_puntuacion = 0
 
    clear()
    apuesta = int(input("Cuanto quieres apostar"))
    banco -= apuesta
    while len(jugador_cartas) < 2:
 
        jugador_carta = random.choice(deck)
        jugador_cartas.append(jugador_carta)
        deck.remove(jugador_carta)
 
        jugador_puntuacion += jugador_carta.carta_value
 
        if len(jugador_cartas) == 2:
            if jugador_cartas[0].carta_value == 11 and jugador_cartas[1].carta_value == 11:
                jugador_cartas[0].carta_value = 1
                jugador_puntuacion -= 10
        
        
        
        print("Tus cartas son: ")
        print_cartas(jugador_cartas, False)
        print("Tu puntuacion es = ", jugador_puntuacion)
 
        input()
 
        crupier_carta = random.choice(deck)
        crupier_cartas.append(crupier_carta)
        deck.remove(crupier_carta)
 
        crupier_puntuacion += crupier_carta.carta_value
 
        print("Las cartas del crupier son : ")
        if len(crupier_cartas) == 1:
            print_cartas(crupier_cartas, False)
            print("La puntuacion del crupier es = ", crupier_puntuacion)
        else:
            print_cartas(crupier_cartas[:-1], True)    
            print("La puntuacion del crupier es = ", crupier_puntuacion - crupier_cartas[-1].carta_value)
 
 
        if len(crupier_cartas) == 2:
            if crupier_cartas[0].carta_value == 11 and crupier_cartas[1].carta_value == 11:
                crupier_cartas[1].carta_value = 1
                crupier_puntuacion -= 10
 
        input()
 
    if jugador_puntuacion == 21:
        print("HAS HECHO BLACKJACK!!!!")
        print("HAS GANADOOOO!!!!")
        banco += apuesta*2.5
        print("ahora tienes este dinero, ", banco)
        quit()
 
    clear()
 
    print("Las cartas del crupier son : ")
    print_cartas(crupier_cartas[:-1], True)
    print("La puntuacion del crupier es = ", crupier_puntuacion - crupier_cartas[-1].carta_value)
 
    print()
 
    print("Tus cartas son: ")
    print_cartas(jugador_cartas, False)
    print("Tu puntuacion es = ", jugador_puntuacion)
 
    while jugador_puntuacion < 21:
        choice = input(" H de Hit or S de Stand : ")
 
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            clear()
            print("Opcion equivocada, elige otra vez")
 
        if choice.upper() == 'H':
 
            jugador_carta = random.choice(deck)
            jugador_cartas.append(jugador_carta)
            deck.remove(jugador_carta)
 
            jugador_puntuacion += jugador_carta.carta_value
 
            c = 0
            while jugador_puntuacion > 21 and c < len(jugador_cartas):
                if jugador_cartas[c].carta_value == 11:
                    jugador_cartas[c].carta_value = 1
                    jugador_puntuacion -= 10
                    c += 1
                else:
                    c += 1
 
            clear()    
 
            print("Las cartas del crupier son : ")
            print_cartas(crupier_cartas[:-1], True)
            print("La puntuacion del crupier es = ", crupier_puntuacion - crupier_cartas[-1].carta_value)
 
            print()
 
            print("Tus cartas son: ")
            print_cartas(jugador_cartas, False)
            print("Tu puntuacion es = ", jugador_puntuacion)
 
        if choice.upper() == 'S':
            break
 
 
    clear()
 
    print("Tus cartas son: ")
    print_cartas(jugador_cartas, False)
    print("Tu puntuacion es = ", jugador_puntuacion)
 
    print()
    print("El crupier revela sus cartas....")
 
    print("Las cartas del crupier son : ")
    print_cartas(crupier_cartas, False)
    print("La puntuacion del crupier es = ", crupier_puntuacion)
 
    if jugador_puntuacion == 21:
        print("HAS HECHO BLACKJACK!!!!")
        banco += apuesta*2.5
        print("ahora tienes este dinero, ", banco)
        quit()
 
    if jugador_puntuacion > 21:
        print("TE HAS PASADO!!! HAS PERDIDO!!!")
        
        print("ahora tienes este dinero, ", banco)
        quit()
 
    input()
 
    while crupier_puntuacion < 17:
        clear()
 
        print("EL CRUPIER DECIDE COGER OTRA CARTA.....")
 
        crupier_carta = random.choice(deck)
        crupier_cartas.append(crupier_carta)
        deck.remove(crupier_carta)
 
        crupier_puntuacion += crupier_carta.carta_value
 
        c = 0
        while crupier_puntuacion > 21 and c < len(crupier_cartas):
            if crupier_cartas[c].carta_value == 11:
                crupier_cartas[c].carta_value = 1
                crupier_puntuacion -= 10
                c += 1
            else:
                c += 1
 
        print("Tus cartas son: ")
        print_cartas(jugador_cartas, False)
        print("Tu puntuacion es = ", jugador_puntuacion)
 
        print()
 
        print("Las cartas del crupier son : ")
        print_cartas(crupier_cartas, False)
        print("La puntuacion del crupier es = ", crupier_puntuacion)      
 
        input()
 
    if crupier_puntuacion > 21:        
        print("EL CRUPIER SE HA PASADO!!! HAS GANADOOOO!!!")
        banco += apuesta*2
        print("ahora tienes este dinero, ", banco)   
        quit()  
 
    if crupier_puntuacion == 21:
        print("EL CRUPIER HA HECHO BLACKJACK!!! HAS PERDIDO")
        
        print("ahora tienes este dinero, ", banco)   
        quit()
 
    if crupier_puntuacion == jugador_puntuacion:
        print("EMPATEEE!!!!")
 
    # Player Wins
    elif jugador_puntuacion > crupier_puntuacion:
        print("HAS GANADO!!!")  
        banco += apuesta*2              
        print("ahora tienes este dinero, ", banco)
    else:
        print("EL CRUPIER GANA!!!")    
        
        print("ahora tienes este dinero, ", banco)          
 
if __name__ == '__main__':
 
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
    cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    cartas_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 
    deck = []
 
    for suit in suits:
 
        for carta in cartas:
 
            deck.append(Carta(suits_values[suit], carta, cartas_values[carta]))
     
    blackjack_game(deck)    
 

