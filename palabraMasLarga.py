#palabra mas larga

#datos
palabra1=input('ingrese la palabra 1: ')

palabra2=input('ingrese la palabra 2: ')

#calculo
letrasPalabra1=len(palabra1)
letrasPalabra2=len(palabra2)
diferencia=letrasPalabra2-letrasPalabra1

#comparacion

if letrasPalabra1>letrasPalabra2:
    if diferencia<0:
        diferencia=-(diferencia)
        print(f"la palabra mas larga es: {palabra1}. Tiene {diferencia} letras más")

elif letrasPalabra2==letrasPalabra1:
    print('las dos palabras tienen el mismo largo.')

else :
    if diferencia<0:
        diferencia=-(diferencia)
        print(f"la palabra mas larga es: {palabra2}. Tiene {diferencia} letras más")