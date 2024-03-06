#determinar si es letra o numero

dato=input('ingrese el dato: ')

#determinar si es texto
if dato.isalpha():
#determinar si es mayuscula
    if dato.isupper():
        print(f"el dato {dato} es letra mayuscula")
    else:
        print(f"el dato {dato} es letra minuscula")

#determinar si es numero
elif dato.isdigit():
    print(f"el dato ingresado {dato} es un numero.")
else:
    print('el dato no es ni numero, ni letra')