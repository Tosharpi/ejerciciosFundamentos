# pedida de datos
num_1 = int(input('ingrese el primer numero: '))
num_2 = int(input('ingrese el segundo numero: '))

# funcion
suma=0
while num_1<num_2-1:
    num_1 = num_1+1
    suma = suma + num_1

print(f"la suma es {suma}")