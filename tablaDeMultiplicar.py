# hacer toda la operacion antes de imprimir
mult =0
val_1 =1
val_2 =2
val_3 =3
val_4 =4
val_5 =5
val_6 =6
val_7 =7
val_8 =8
val_9 =9
val_10 =10
while mult<10:
    mult +=1
    for val in range(1, 11):
        result = str(val * mult).rjust(2) 
        print(' '.join(result))

