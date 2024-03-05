#huevos a la copa (matenme)

from math import *

t0 = float(input("Ingrese la temperatura original del huevo: "))

#datos
M = 67

c = 3.7

ro = 1.038

K = 0.0054

tw = 100

ty = 70

#calculo
t = ((M**(2/3) * c * ro**(1/3)) / (K * 3.1416**2 * ((4 * 3.1416 / 3)**(2/3)))) * log(0.76 * ((t0 - tw) / (ty - tw)))

print(f"El tiempo necesario para preparar el huevo a la copa es de aproximadamente {t:.2f} segundos.")