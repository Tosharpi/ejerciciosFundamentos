#índice de masa corporal

estatura = float(input('ingrese su estatura en metros '))
edad = int(input('ingrese su edad: '))
peso = float(input('ingrese su peso en kilos: '))

IMC = peso / (estatura**2)

if edad<45:
    if IMC < 22:
        print(f"su condicion de riesgo es {IMC}. Su riesgo es bajo.")
    elif IMC>=22:
        print(f"su condicion de riesgo es {IMC}. Su riesgo es medio")
elif edad>=45:
    if IMC < 22:
        print(f"su condicion de riesgo es {IMC}. Su riesgo es medio.")
    elif IMC>=22:
        print(f"su condicion de riesgo es {IMC}. Su riesgo es alto")