#ingrese un numero para generar la tabla

num = int(input('ingrese el numero: '))

cont=1
while cont<=10:
    tabla=cont*num
    print(f"{num} x {cont} = {tabla}")
    cont += 1