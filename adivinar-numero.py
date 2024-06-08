from random import randint

print('*** Bienvenido al juego adivina tu numero secreto  ***')

numero_secreto = randint(1, 50)
intentos = 0
maximo_intentos =5

adivinanza = None

# Mientras el usuario no haya adivinado el número secreto y tenga intentos
while adivinanza != numero_secreto and intentos < maximo_intentos: 
    adivinanza = int(input("Adivina el número secreto entre 1 y 50: "))
    intentos += 1                   
    
    # Si el usuario ha agotado todos los intentos
    
    if intentos == maximo_intentos:
                 
        print("Lo siento has agotado todos tus intentos ")
        
        print( f'El numero secreto que hubieras advinado es: {numero_secreto}')
        # Salir del bucle
        break
   
   # Si el usuario no ha adivinado el número secreto y le quedan intentos     
    if adivinanza != numero_secreto and intentos < maximo_intentos:
        intentos_restantes = maximo_intentos - intentos
        print(f"Te quedan {intentos_restantes} intentos por realizar")

    # Si el usuario no ha adivinado el número secreto
    if adivinanza < numero_secreto:
        print("El número secreto es mayor")
    elif adivinanza > numero_secreto:
        print("El número secreto es menor")
        
# Si el usuario ha adivinado el número secreto       
if adivinanza == numero_secreto:
   print( f'Felicidades , adivinastes el número secreto en {intentos} intentos')
