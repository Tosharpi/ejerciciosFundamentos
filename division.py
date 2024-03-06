#division

#datos

numero1=int(input('ingrese el primer numero: '))
numero2=int(input('ingrese el segundo numero: '))

#formula

division=(numero1/numero2)
resto=division%1
cociente=int(division)

#comprobacion e impresion

if division%1==0:

    print(f"la division es exacta. el cociente es: {cociente} el resto es: {resto}")


else:
    print(f"la division no es exacta. el cociente es: {cociente} el resto es: {resto}")