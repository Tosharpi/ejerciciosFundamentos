duracionTramo=0
duracionTotalTramo=0
horas=0

while True:

    duracionTramo = int(input('Duracion de tramo: '))
    duracionTotalTramo +=duracionTramo
    if duracionTramo == 0:
        break

# conversion
while duracionTotalTramo > 60:
    duracionTotalTramo -= 60
    horas += 1

minutos = duracionTotalTramo

if horas>0:
    print(f"Tiempo total de viaje: {horas}:{minutos} horas")
else:
    print(f"Tiempo total de viaje: 0:{minutos}")