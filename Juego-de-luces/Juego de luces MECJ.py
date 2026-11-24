import numpy as np
import random

#Genera la posicion inicial de las luces
cantidad = 10
while True:
    luces = np.zeros(cantidad, dtype=np.uint8)

    for posicion in range(cantidad):
        if np.random.randint(2) == 1:
            if posicion > 0:
                luces[posicion - 1] = 1-luces[posicion - 1]
            if posicion < cantidad - 1:
                luces[posicion + 1] = 1-luces[posicion + 1]
            luces[posicion] = 1-luces[posicion]

    
    if np.any(luces == 1):
        break

while True:
    
    print("\nPosición:", end=" ")
    for i in range(luces.size):
        print(f"{i + 1:>3}", end=" ")

    print("\nEstado:  ", end=" ")
    for i in range(luces.size):
        print(f"{luces[i]:>3}", end=" ")
    
    
    print()
    
    try:
        posicion = int(input("Que luz deseas seleccionar (1-10): "))

        if posicion >= 1 and posicion <= cantidad:
            posicion -= 1           
            luces[posicion] = 1 - luces[posicion]

            
            if posicion > 0:
                luces[posicion - 1] = 1 - luces[posicion - 1]

            if posicion < cantidad - 1:
                luces[posicion + 1] = 1 - luces[posicion + 1]

            
            if np.all(luces == 0):
                print("\nFelicidades apagaste todas las luces.")
                break

        else:
            print("Posicion no valida.")

    except ValueError:
        print("Debes introducir un numero.")