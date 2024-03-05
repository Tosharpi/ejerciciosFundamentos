#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
#entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

horaActual=int(input('ingresa solo la hora militar actual: '))

horaFutura=int(input('ingresa cuanto tiempo quieres que transcurra según la hora actual: '))


horaFuturaReal=horaActual+horaFutura


while horaFuturaReal>24:
    
    horaFuturaReal= horaFuturaReal - 24

print(f"""la hora mas adelante será: {horaFuturaReal}""")

