#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario

numero=float(input('ingresa el numero: '))

if numero>1:

    while numero>1 :
        numero=numero-1

elif numero<(-1):

    while numero<(-1) :
        numero=numero+1


print(f"""la parte decimal es {numero}""")