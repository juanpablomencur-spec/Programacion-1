import random
valores = ["A", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "J", "Q", "K"]

palos = ["♥", "♦", "♣", "♠"]

def calcular_puntuacion(mano):
    # Calcula la puntuacion de una mano de Blackjack, teniendo en cuenta el valor de los ases
    puntos = 0
    ases = 0

    for carta in mano:
        valor = carta[0]

        if valor == "A":
            puntos += 11
            ases += 1

        elif valor in ["J", "Q", "K"]:
            puntos += 10

        else:
            puntos += int(valor)

   
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
    return puntos


def es_blackjack_bonus(mano):
    return (len(mano) == 2 and calcular_puntuacion(mano) == 21 and ["A", "♠"] in mano and (["J", "♠"] in mano or ["J", "♣"] in mano))
#-----------------------------------------------------------
while True:
    try:
        saldo = int(input("Con cuanto dinero vas a entrar al juego? = "))
        
        if saldo > 0:
            break
        else:
            print("ERROR: No puedes jugar con saldo negativo")
        
    except ValueError:
        print("ERROR: Tienes que ingresar una cantidad")
        

while saldo > 0:
    
    print("Saldo actual:", saldo)
    print("-----------------------------")
    baraja = [
        [valor, palo]
        for palo in palos
        for valor in valores
    ]
    random.shuffle(baraja)

    mano_jugador = []
    mano_dealer = []
    
    while True:
        try:
            apuesta = int(input("Cuanto quieres apostar? = "))
            
            if apuesta > 0 and apuesta <= saldo:
                break
            else:
        
                if apuesta > saldo:
                    print("ERROR: Tu apuesta es mayor a tu saldo")
                
                elif apuesta < 1:
                    print("ERROR: Tu apuesta debe ser mayor a 0 ")
                
        except ValueError:
            print("ERROR: Debes de ingresar una apuesta ")
         
    print()
    for i in range(2):
        mano_jugador.append(baraja.pop())
        mano_dealer.append(baraja.pop())
        
    print("Cartas del jugador:")
    
    for carta in mano_jugador:
        print(carta[0], carta[1])
        
    print("Puntuación:", calcular_puntuacion(mano_jugador))
    puntos_jugador = calcular_puntuacion(mano_jugador)

    print("\nCartas del dealer:")
    print(mano_dealer[0][0], mano_dealer[0][1])
    print("Carta oculta")
    print("Puntuación:", calcular_puntuacion([mano_dealer[0]]))
    puntos_dealer = calcular_puntuacion(mano_dealer)

    print("\nCartas restantes:", len(baraja))
   
    
    blackjack_jugador = (len(mano_jugador) == 2 and calcular_puntuacion(mano_jugador) == 21)
    blackjack_dealer = (len(mano_dealer) == 2 and calcular_puntuacion(mano_dealer) == 21)
    
    resultado = ""
    
    
    if blackjack_dealer == True:
        print("\nCartas del Dealer:")

        for carta in mano_dealer:
            print(carta[0], carta[1])

        print("Puntuación:", calcular_puntuacion(mano_dealer))

        if blackjack_jugador == True:
            print("Ambos tienen blackjack, queda en empate")
            resultado = "empate"

        else:
            print("El dealer tiene blackjack. Pierdes la apuesta.")
            resultado = "dealer"

    elif blackjack_jugador == True:
        if es_blackjack_bonus(mano_jugador):
            print("BLACKJACK BONUS, ganaste la ronda")
        else:
            print("Blackjack, ganaste la ronda")

        resultado = "jugador"
    
    else:
        while True:
            if puntos_jugador > 21:
                print("Perdiste, te pasaste de 21")
                resultado = "dealer"
                break
            
            if puntos_jugador == 21:
                print("Llegaste a 21, turno del dealer")
                break
            
            print()
            accion = input("Quieres pedir o plantarte? [p/s] = ").strip().lower()
            
            if accion == "p":
                mano_jugador.append(baraja.pop())
                print()
                print("Cartas del jugador:")
    
                for carta in mano_jugador:
                    print(carta[0], carta[1])
        
                print("Puntuación:", calcular_puntuacion(mano_jugador))
                puntos_jugador = calcular_puntuacion(mano_jugador)
            
            elif accion == "s":
                print("Te plantas")
                break

            else:
                print("Opción no válida. Escribe p o s.")

        if resultado != "dealer" and blackjack_jugador == False:
            print("\nCartas del dealer:")

            for carta in mano_dealer:
                print(carta[0], carta[1])

            print("Puntuación:", calcular_puntuacion(mano_dealer))
            puntos_dealer = calcular_puntuacion(mano_dealer)
            
            while calcular_puntuacion(mano_dealer) < 17:
                mano_dealer.append(baraja.pop())
                
                print("\nEl dealer saca carta")
                print("Cartas del dealer:")

                for carta in mano_dealer:
                    print(carta[0], carta[1])
                    
            print("Puntuación:", calcular_puntuacion(mano_dealer))
            puntos_dealer = calcular_puntuacion(mano_dealer)
            
            puntos_jugador = calcular_puntuacion(mano_jugador)

            if puntos_dealer > 21:
                print("El dealer se pasó de 21 ganaste")
                resultado = "jugador"

            elif puntos_jugador > puntos_dealer:
                print("Ganaste por tener mas puntos que el dealer")
                resultado = "jugador"

            elif puntos_jugador < puntos_dealer:
                print("Perdiste el dealer tiene mas puntos.")
                resultado = "dealer"

            else:
                print("Empate ambos tienen la misma puntuacion")
                resultado = "empate"
                
                
                
                
    if resultado == "jugador":
        if es_blackjack_bonus(mano_jugador) and blackjack_jugador:
                saldo += apuesta * 2
        else:
            saldo += apuesta

    elif resultado == "dealer":
        saldo -= apuesta

    elif resultado == "empate":
        print("Se devuelve la apuesta.")
            
    print("-----------------------------")
    print("Saldo actual:", saldo)
        
    if saldo <= 0:
        print("Te has quedado sin saldo.")
        break
    
        
    respuesta = input("¿Quieres volver a jugar? [s/n]: ").strip().lower()
    if respuesta != "s":
        print()
        print("Gracias por jugar")
        print("Saldo final:", saldo)
        break
    
    
