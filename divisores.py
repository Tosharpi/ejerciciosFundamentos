num = int(input('ingrese el numero a dividir: '))
divisores = []
for val in range(1, num+1):

    if 200%val == 0:
        divisores.append(val)

print(f"los divisores de {num} son: {divisores}")
