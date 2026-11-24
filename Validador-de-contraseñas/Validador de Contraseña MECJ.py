def validador_contraseña(cadena):
    ind_letra_mayuscula = False
    ind_letra_minuscula = False
    ind_digito = False
    ind_caracter_especial = False

    for i in range( len(cadena) ):
      if cadena[i] in 'abcdefghuiklmnopqrstuvwxyz':
        ind_letra_minuscula = True
      elif cadena[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        ind_letra_mayuscula = True
      elif cadena[i] in '0123456789':
        ind_digito = True
      elif  cadena[i] in '!"#$%&?¡=)(/*-+_':
        ind_caracter_especial = True
    
    if len(cadena)>=5 and ind_letra_mayuscula and ind_letra_minuscula and ind_digito and ind_caracter_especial:
        return True
    else:
        return False

#-------------------------------------------
        
while True:
    cadena = input("Escribe una cadena: ")

    if len(cadena)>0:
        break
    else:
        print("ERROR: No puede quedar vacío.")
        
    
es_contraseña_segura = validador_contraseña(cadena)

if es_contraseña_segura == True:
    print("Tu contraseña es segura")
else:
    print("Tu contraseña no es segura")
        
    