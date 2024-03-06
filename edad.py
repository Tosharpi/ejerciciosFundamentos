#edad del usuario

from time import localtime
t = localtime()
t.tm_mday

t.tm_mon

t.tm_year

cont = 1

while cont ==1:

    dia=int(input('ingrese el dia de su nacimiento: '))
    if dia>31 or dia<1 :
        break
    mes=int(input('ingrese el mes de su nacimiento: '))
    if mes>12 or mes<1 :
        break
    año=int(input('ingrese el año de su nacimiento: '))
    if año>t.tm_year:
        break
    cont=cont+1

#print(t.tm_mday, t.tm_mon, t.tm_year)

edad=t.tm_year-año
edad=edad-1
if dia<t.tm_mday and mes<t.tm_mon :
    edad=edad+1
print(edad)
