#numeros de menor a mayor
numero=1
numeros=[]

for i in range(4):
    numeroIngresado=int(input(f"ingrese el numero:  {numero}"))
    numero=numero+1
    numeros.append(numeroIngresado)

    numerosOrdenados=sorted(numeros)
print(f"los numeros ordenados de mayor a menor serian: {numerosOrdenados}")