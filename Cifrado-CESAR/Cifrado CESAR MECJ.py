def cifrar(mensaje, desplazamiento):
    abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    for letra in mensaje:
        if letra in abecedario:
            for i in range(len(abecedario)):
                if letra == abecedario[i]:
                    posicion = i + desplazamiento

                    while posicion >= len(abecedario):
                        posicion -= 26

                    resultado += abecedario[posicion]
                    break
        else:
            resultado += letra

    return resultado


mensaje = input("Escribe un mensaje: ")
desplazamiento = int(input("Desplazamiento: "))

print("Mensaje cifrado:", cifrar(mensaje, desplazamiento))