#calcular el promedio de tres datos

certamen1 = int(input("Ingrese nota certamen 1: "))
certamen2 = int(input("Ingrese nota certamen 2: "))
notaLab = int(input("Ingrese nota laboratorio: "))

notaNecesaria = (59.5 - 0.3 * notaLab) / 0.7
certamen3 = 3 * notaNecesaria - (certamen1 + certamen2) + 1

print("Necesita nota", int(round(certamen3)), "en el certamen 3")