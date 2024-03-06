#calculadora

#datos
numero1=float(input('ingrese el primer numero: '))
numero2=float(input('ingrese el segundo numero: '))
operacion=input('ingrese el operador (+ , - , * , /)')

#comprobacion
if operacion=='+':
    resultado=numero1+numero2

elif operacion=='-':
    resultado=numero1-numero2

elif operacion=='*':
    resultado=numero1*numero2

elif operacion=='/':
    resultado=numero1/numero2

#salida
print(f"el resultado es: {resultado}")