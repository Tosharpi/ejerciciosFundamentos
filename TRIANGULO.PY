#triangulos

#ingreso de datos
print('ingrese los lados: ')
ladoA=float(input('lado A: '))
ladoB=float(input('lado B: '))
ladoC=float(input('lado C: '))

#descarte
if (ladoA+ladoB)>ladoC:
    print('triangulo no valido. ')
elif (ladoC+ladoB)>ladoA:
    print('triangulo no valido. ')
elif (ladoA+ladoC)>ladoB:
    print('triangulo no valido. ')

#tipo de triangulo y salida
if ladoA == ladoB == ladoC:
    print("El triángulo es equilátero")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("El triángulo es isósceles")
else:
    print('el triangulo es escaleno')